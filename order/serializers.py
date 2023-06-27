from rest_framework import serializers
from shops.models import Product
from .models import Order, OrderItem
from django.db.models import F, Sum


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "price"]


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = ["id", "product", "quantity"]


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, order):
        total_price = order.items.annotate(
            item_total_price=F("quantity") * F("product__price")
        ).aggregate(total_price=Sum("item_total_price"))["total_price"]
        return total_price or 0

    class Meta:
        model = Order
        fields = ["id", "placed_at", "status", "owner", "items", "total_price"]
