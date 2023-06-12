from rest_framework import serializers
from .models import Category, Product
from django.utils.text import slugify


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ["slug"]

    def create(self, validated_data):
        name = validated_data.get("name")
        validated_data["slug"] = slugify(name)
        instance = super().create(validated_data)
        return instance

    def update(self, instance, validated_data):
        name = validated_data.get("name", instance.name)
        slug = slugify(name)
        instance.name = name
        instance.slug = slug
        instance.save()
        return instance


class ProductReadSerializer(serializers.ModelSerializer):
    category = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name="category-detail",
        lookup_field="slug",
        lookup_url_kwarg="slug",
    )

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "category",
            "image",
            "price",
            "available",
        ]


class ProductWriteSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Product
        exclude = ["slug"]

    def create(self, validated_data):
        name = validated_data.get("name")
        validated_data["slug"] = slugify(name)
        instance = super().create(validated_data)
        return instance


class ProductDetailsSerializer(serializers.ModelSerializer):
    category = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name="category-detail",
        lookup_field="slug",
        lookup_url_kwarg="slug",
    )

    class Meta:
        model = Product
        fields = "__all__"

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)

        if "name" in validated_data:
            instance.slug = slugify(instance.name)

        for attr, value in validated_data.items():
            if attr not in ["name", "slug"]:
                setattr(instance, attr, value)

        instance.save()
        return instance
