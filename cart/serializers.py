from rest_framework import serializers
from shops.models import Product
from .models import Cart, CartItem
from django.db.models import F, Sum


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "price"]


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ["id", "product", "quantity"]


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, cart):
        total_price = cart.items.annotate(
            item_total_price=F("quantity") * F("product__price")
        ).aggregate(total_price=Sum("item_total_price"))["total_price"]
        return total_price or 0

    class Meta:
        model = Cart
        fields = ["id", "user", "created_at", "items", "total_price"]
