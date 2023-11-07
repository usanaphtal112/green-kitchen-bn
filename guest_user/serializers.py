from rest_framework import serializers


class GuestCartProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(source="product.id")
    name = serializers.CharField(source="product.name")
    price = serializers.DecimalField(
        source="product.price", max_digits=8, decimal_places=2
    )
    image = serializers.ImageField(source="product.image")
    created_by = serializers.StringRelatedField()

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["price"] = str(representation["price"])
        return representation


class CartItemSerializer(serializers.Serializer):
    product = GuestCartProductSerializer()
    quantity = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    sub_total_price = serializers.DecimalField(max_digits=8, decimal_places=2)
