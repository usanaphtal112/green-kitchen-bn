from rest_framework import serializers
from .models import Category, Product
from django.utils.text import slugify
from cloudinary import uploader


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
            "created_by",
        ]


class ProductWriteSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    image = serializers.ImageField(required=False)

    class Meta:
        model = Product
        exclude = ["slug"]

    def create(self, validated_data):
        name = validated_data.get("name")
        validated_data["slug"] = slugify(name)

        image = validated_data.pop("image", None)
        # if image:
        #     result = uploader.upload(image)
        #     validated_data["image"] = result["secure_url"]

        instance = super().create(validated_data)
        return instance


class ProductDetailsSerializer(serializers.ModelSerializer):
    category = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name="category-detail",
        lookup_field="slug",
        lookup_url_kwarg="slug",
    )
    image = serializers.ImageField(required=False)

    class Meta:
        model = Product
        fields = "__all__"

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)

        if "name" in validated_data:
            instance.slug = slugify(instance.name)

        image = validated_data.pop("image", None)
        # if image:
        #     result = uploader.upload(image)
        #     instance.image = result["secure_url"]

        for attr, value in validated_data.items():
            if attr not in ["name", "slug", "image"]:
                setattr(instance, attr, value)

        instance.save()
        return instance
