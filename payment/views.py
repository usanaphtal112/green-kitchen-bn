from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.db.models import Sum
from .models import Payment
from cart.models import Cart, CartItem
from guest_user import guest_cart
from order.models import Order, OrderItem
from django.http import JsonResponse
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

            cart_items = cart.cart.items.all()
            print("cart_items: ", cart_items)
            # Prepare line items for the cart items
            for item in cart_items:
                print("item: ", item)
                line_items.append(
                    {
                        "price_data": {
                            "currency": "INR",
                            "product_data": {
                                "name": item.name,
                                "images": [f"{settings.API_URL}/{item.product.image}"],
                            },
                            "unit_amount": item.price,
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


class GuestCreateCheckoutSession(APIView):
    def post(self, request):
        # Fetch cart items from the session
        cart = guest_cart.Cart(request)
        cart_items = list(cart)

        if not cart_items:
            return Response(
                {"error": "No items in the cart. Add items to procceed with the order"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        # print("cart_items: ", cart_items)

        # Get the base URL
        base_url = request.build_absolute_uri("/")
        line_items = []
        for cart_item in cart_items:
            product_data = cart_item["product"]
            print("product_data product_data: ", product_data)
            print("Cart items: ", cart_item)
            product = cart_item["product"]
            quantity = cart_item["quantity"]
            price = cart_item["price"]
            image_url = base_url[:-1] + product_data["image"]
            product_data["image"] = image_url
            print("image_url image_url image_url image_url: ", image_url)

            # Create a Stripe line item dictionary
            line_item = {
                "price_data": {
                    "currency": "INR",
                    "unit_amount": int(float(price) * 100),
                    "product_data": {
                        "name": product["name"],
                        "images": [image_url],
                    },
                },
                "quantity": quantity,
            }
            line_items.append(line_item)

        success_url = "http://localhost:5173/checkout/success/"
        cancel_url = "http://localhost:5173/checkout/failed/"

        # Create a Stripe Checkout Session
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            mode="payment",
            line_items=line_items,
            success_url=success_url,
            cancel_url=cancel_url,
        )

        # Retrieve the session ID to redirect the user to the Stripe checkout page
        session_id = checkout_session.id
        print("session_id: ", session_id)
        print("checkout_session.url: ", checkout_session.url)

        # Redirect the user to the Stripe checkout page
        return redirect(checkout_session.url, code=303)


class WebHook(APIView):
    def post(self, request):
        event = None
        payload = request.body
        print("Header Header: ", request.META)
        sig_header = request.META["HTTP_STRIPE_SIGNATURE"]
        # sig_header = request.headers.get("stripe-signature")
        print("sig_header: ", sig_header)

        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, settings.STRIPE_SECRET_WEBHOOK
            )
        except ValueError as err:
            # Invalid payload
            raise err
        except stripe.error.SignatureVerificationError as err:
            # Invalid signature
            raise err

        # Handle the event
        if event.type == "payment_intent.succeeded":
            payment_intent = event.data.object
            print("--------payment_intent ---------->", payment_intent)
        elif event.type == "payment_method.attached":
            payment_method = event.data.object
            print("--------payment_method ---------->", payment_method)
        # ... handle other event types
        else:
            print("Unhandled event type {}".format(event.type))

        return JsonResponse(success=True, safe=False)


@csrf_exempt
def stripe_webhook_view(request):
    payload = request.body
    # print(payload.body)
    # sig_header = request.META["HTTP_STRIPE_SIGNATURE"]
    sig_header = request.headers.get("stripe-signature")
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
