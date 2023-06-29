from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Sum
from .models import Payment
from cart.models import Cart, CartItem
from order.models import Order, OrderItem
from shops.models import Product
from drf_spectacular.utils import extend_schema
from django.views.decorators.csrf import csrf_exempt
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


@extend_schema(
    description="Stripe checkout sessios",
    tags=["Payment"],
)
class CreateCheckOutSession(APIView):
    def post(self, request, *args, **kwargs):
        try:
            # Retrieve the cart for the current user
            cart = Cart.objects.get(user=request.user)

            line_items = []
            total_price = 0

            # Prepare line items for the cart items
            for item in cart.items.all():
                line_items.append(
                    {
                        "price_data": {
                            "currency": "INR",
                            "unit_amount": int(item.product.price) * 100,
                            "product_data": {
                                "name": item.product.name,
                                "images": [f"{settings.API_URL}/{item.product.image}"],
                            },
                        },
                        "quantity": item.quantity,
                    }
                )
                total_price += item.product.price * item.quantity

            # Create a Checkout Session with the line items
            checkout_session = stripe.checkout.Session.create(
                line_items=line_items,
                metadata={"cart_id": cart.id},
                mode="payment",
                success_url=settings.SITE_URL + "?success=true",
                cancel_url=settings.SITE_URL + "?canceled=true",
            )

            # Create a Payment record

            print(checkout_session)
            Payment.objects.create(
                cart_id=cart.id,
                amount=total_price,
                # client_secret=checkout_session.client_secret,
            )

            return redirect(checkout_session.url)
        except Exception as e:
            return Response(
                {
                    "msg": "Something went wrong while creating the Stripe session",
                    "error": str(e),
                },
                status=500,
            )


@csrf_exempt
def stripe_webhook_view(request):
    payload = request.body
    # print(payload.body)
    sig_header = request.META["HTTP_STRIPE_SIGNATURE"]
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_SECRET_WEBHOOK
        )
    except ValueError as e:
        # Invalid payload
        return Response(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return Response(status=400)

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        cart_id = session["metadata"]["cart_id"]
        customer_email = session["customer_details"]["email"]

        try:
            cart = Cart.objects.get(id=cart_id)
            order = Order.objects.create(owner=cart.user)

            for item in cart.items.all():
                OrderItem.objects.create(
                    order=order, product=item.product, quantity=item.quantity
                )

            # Sending confirmation email
            send_mail(
                subject="Payment successful",
                message=f"Thank you for your purchase. Your order is ready.",
                recipient_list=[customer_email],
                from_email="naphtaldanny@gmail.com",
            )

            # Mark the payment as paid
            order.status = "Paid"
            order.save()

            # Mark the payment as paid
            Payment.objects.filter(cart_id=cart_id).update(paid=True)

            # Clear the cart
            cart.items.all().delete()
            cart.delete()
        except Cart.DoesNotExist:
            pass

    return HttpResponse(status=200)
