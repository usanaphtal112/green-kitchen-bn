from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .guest_cart import Cart
from .serializers import CartItemSerializer, GuestCartProductSerializer
from django.conf import settings
from shops.models import Product
from .models import GuestOrder, GuestOrderItem
from .forms import UserDetailForm
from drf_spectacular.utils import extend_schema


@extend_schema(
    description="Items cart",
    tags=["Guest User"],
)
class CartAPIView(APIView):
    def get(self, request):
        cart = Cart(request)
        cart_items = list(cart)  # Convert the cart generator to a list

        # Calculate total price
        total_price = cart.get_total_price()

        # Get the base URL
        base_url = request.build_absolute_uri("/")

        # Prepare serialized cart items
        serialized_cart_items = []
        for cart_item in cart_items:
            product_data = cart_item["product"]
            image_url = (
                base_url[:-1] + product_data["image"]
            )  # Construct full image URL
            product_data["image"] = image_url  # Update the image URL
            serialized_cart_item = {
                "product": product_data,
                "quantity": cart_item["quantity"],
                "price": cart_item["price"],
                "sub_total_price": cart_item["sub_total_price"],
            }
            serialized_cart_items.append(serialized_cart_item)

        # Include total price in the response
        data = {
            "cart_items": serialized_cart_items,
            "total_price": total_price,
        }
        return Response(data)


@extend_schema(
    description="Items cart",
    tags=["Guest User"],
)
class CartDetailsAPIViews(APIView):
    def post(self, request, product_id):
        # product_id = request.data.get("product_id")
        # print("Received product ID:", product_id)
        quantity = int(request.data.get("quantity", 1))
        override_quantity = bool(request.data.get("override_quantity", False))

        try:
            product = Product.objects.get(id=product_id)
            cart = Cart(request)
            cart.add(product, quantity, override_quantity)
            return Response(status=201)
        except Product.DoesNotExist:
            return Response({"error": "Invalid product ID"}, status=400)

    def delete(self, request, product_id):
        # product_id = request.data.get("product_id")

        try:
            product = Product.objects.get(id=product_id)
            cart = Cart(request)
            cart.remove(product)
            return Response(status=204)
        except Product.DoesNotExist:
            return Response({"error": "Invalid product ID"}, status=400)

    def patch(self, request, product_id):
        # product_id = request.data.get("product_id")
        quantity = int(request.data.get("quantity"))

        try:
            product = Product.objects.get(id=product_id)
            cart = Cart(request)
            cart.add(product, quantity, override_quantity=True)
            return Response(status=200)
        except Product.DoesNotExist:
            return Response({"error": "Invalid product ID"}, status=400)


@extend_schema(
    description="Guest user Order",
    tags=["Guest User"],
)
class PlaceOrderAPIView(APIView):
    def post(self, request):
        # Validate and process user details
        user_detail_form = UserDetailForm(request.data)
        if user_detail_form.is_valid():
            user_data = user_detail_form.cleaned_data

            # Fetch cart items from the session
            cart = Cart(request)
            cart_items = list(cart)

            if not cart_items:
                return Response(
                    {
                        "error": "No items in the cart. Add items to procceed with the order"
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # Create a new GuestOrder instance
            order = GuestOrder.objects.create(
                full_name=user_data["full_name"],
                phone_number=user_data["phone_number"],
                district=user_data["district"],
                sector=user_data["sector"],
                address=user_data["address"],
                payment_method=user_data["payment_method"],
                message=user_data["message"],
            )

            # Loop through cart items and create GuestOrderItem instances
            for cart_item in cart_items:
                product_id = cart_item.get("product_id")
                quantity = cart_item.get("quantity")
                try:
                    product = Product.objects.get(id=product_id)
                    GuestOrderItem.objects.create(
                        guest_order=order,
                        product=product,
                        quantity=quantity,
                        price=product.price,
                    )
                except Product.DoesNotExist:
                    return Response(
                        {"error": f"Product with ID {product_id} does not exist"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

            request.session.pop(settings.CART_SESSION_ID, None)

            return Response(
                {"message": "Order placed successfully"}, status=status.HTTP_201_CREATED
            )
        else:
            return Response(user_detail_form.errors, status=status.HTTP_400_BAD_REQUEST)
