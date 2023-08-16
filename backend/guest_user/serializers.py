from rest_framework import serializers
from shops.models import Product
from .models import GuestOrder, GuestOrderItem


class ProductSerializer(serializers.ModelSerializer):
    # image = serializers.ImageField(use_url=True)

    class Meta:
        model = Product
        fields = ["id", "name", "price"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["price"] = str(representation["price"])
        return representation


class CartItemSerializer(serializers.Serializer):
    product = ProductSerializer()
    quantity = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    sub_total_price = serializers.DecimalField(max_digits=8, decimal_places=2)
