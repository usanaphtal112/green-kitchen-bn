from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Product, Category
from .serializers import (
    CategorySerializer,
    ProductDetailsSerializer,
    ProductReadSerializer,
    ProductWriteSerializer,
)
from drf_spectacular.utils import extend_schema
from django.utils.text import slugify


@extend_schema(
    description="List of products",
    tags=["Products"],
)
class ProductAPIView(generics.ListCreateAPIView):
    serializer_class = ProductWriteSerializer

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ProductReadSerializer
        return ProductWriteSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        category_slug = self.request.query_params.get("category_slug")
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)
        return queryset


@extend_schema(
    description="Product details",
    tags=["Products"],
)
class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailsSerializer


@extend_schema(
    description="Category List",
    tags=["Product Category"],
)
class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


@extend_schema(
    description="Product category details",
    tags=["Product Category"],
)
class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "slug"
