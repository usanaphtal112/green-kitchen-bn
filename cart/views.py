from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Cart, CartItem
from shops.models import Product
from shops.permissions import IsBuyerRoleOnly
from .serializers import CartSerializer, CartItemSerializer
from drf_spectacular.utils import extend_schema


@extend_schema(
    description="Items cart",
    tags=["Cart"],
)
class CartView(APIView):
    permission_classes = [IsAuthenticated, IsBuyerRoleOnly]

    def get(self, request):
        try:
            cart = Cart.objects.get(user=request.user)
        except Cart.DoesNotExist:
            return Response({"error": "You don't have any product in cart"}, status=404)

        serializer_class = CartSerializer(cart)
        return Response(serializer_class.data)

    # def post(self, request):
    #     try:
    #         cart = Cart.objects.get(user=request.user)
    #     except Cart.DoesNotExist:
    #         cart = Cart.objects.create(user=request.user)

    #     serializer_class = CartSerializer(cart)
    #     return Response(serializer_class.data)


@extend_schema(
    description="Add Product to Cart",
    tags=["Cart"],
)
class CartItemView(APIView):
    permission_classes = [IsAuthenticated, IsBuyerRoleOnly]

    def post(self, request, product_id):
        try:
            cart = Cart.objects.get(user=request.user)
        except Cart.DoesNotExist:
            cart = Cart.objects.create(user=request.user)
        # product_id = request.data.get("product_id")
        quantity = request.data.get("quantity", 1)

        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=400)

        # Check if the product is already in the cart
        existing_item = CartItem.objects.filter(cart=cart, product=product).first()
        if existing_item:
            return Response({"message": "Product already exists in the cart."})
        # if existing_item:
        #     existing_item.quantity += int(quantity)
        #     existing_item.save()
        else:
            CartItem.objects.create(cart=cart, product=product, quantity=quantity)

        cart_serializer = CartSerializer(cart)
        return Response(cart_serializer.data)


@extend_schema(
    description="Update quantity or remove item from cart",
    tags=["Cart"],
)
class CartItemDetailsView(APIView):
    permission_classes = [IsAuthenticated, IsBuyerRoleOnly]

    def put(self, request, item_id):
        try:
            item = CartItem.objects.get(pk=item_id, cart__user=request.user)
        except CartItem.DoesNotExist:
            return Response({"error": "Cart item not found"}, status=400)

        quantity = request.data.get("quantity", 1)
        item.quantity = int(quantity)
        item.save()

        cart = Cart.objects.get(user=request.user)
        cart_serializer_class = CartSerializer(cart)
        return Response(cart_serializer_class.data)

    def delete(self, request, item_id):
        try:
            item = CartItem.objects.get(pk=item_id, cart__user=request.user)
        except CartItem.DoesNotExist:
            return Response({"error": "Cart item not found"}, status=400)

        item.delete()

        cart = Cart.objects.get(user=request.user)
        cart_serializer_class = CartSerializer(cart)
        return Response(cart_serializer_class.data)
