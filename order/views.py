from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Order, OrderItem
from shops.models import Product
from shops.permissions import IsBuyerRoleOnly
from cart.models import Cart
from .serializers import OrderSerializer, OrderItemSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from drf_spectacular.utils import extend_schema


@extend_schema(
    description="Order operations",
    tags=["Orders"],
)
class UserOrdersAPIView(APIView):
    # permission_classes = [IsAuthenticated, IsBuyerRoleOnly]

    def get(self, request):
        orders = Order.objects.filter(owner=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        # cart_id = request.data.get("cart_id")  # Get the cart ID from the request data
        # # Verify if the cart belongs to the currently logged-in user
        # cart = get_object_or_404(Cart, id=cart_id, user=request.user)

        try:
            cart = Cart.objects.get(user=request.user)
        except Cart.DoesNotExist:
            return Response({"error": "No product selected into Cart."}, status=400)

        items = cart.items.all()

        if not items:
            return Response({"error": "Your cart is empty"}, status=400)

        order = Order.objects.create(owner=request.user)

        for item in items:
            OrderItem.objects.create(
                order=order, product=item.product, quantity=item.quantity
            )

        cart.delete()

        order_serializer = OrderSerializer(order)
        return Response(order_serializer.data)


@extend_schema(
    description="Update order",
    tags=["Orders"],
)
class OrderDetailsAPIView(APIView):
    # permission_classes = [IsAuthenticated, IsBuyerRoleOnly]

    def get(self, request, order_id):
        try:
            order = Order.objects.get(pk=order_id, owner=request.user)
        except Order.DoesNotExist:
            return Response({"error": "Order not found"}, status=400)

        order_serializer = OrderSerializer(order)
        return Response(order_serializer.data)

    def put(self, request, order_id):
        try:
            order = Order.objects.get(pk=order_id, owner=request.user)
        except Order.DoesNotExist:
            return Response({"error": "Order not found"}, status=400)

        # Update the order status
        status = request.data.get("status")
        order.status = status
        order.save()

        order_serializer = OrderSerializer(order)
        return Response(order_serializer.data)

    def delete(self, request, order_id):
        try:
            order = Order.objects.get(pk=order_id, owner=request.user)
        except Order.DoesNotExist:
            return Response(
                {"error": "Order not found"}, status=status.HTTP_400_BAD_REQUEST
            )

        order.status = "Cancelled"
        order.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
