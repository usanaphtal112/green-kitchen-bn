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
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from .permissions import IsSellerOrReadOnly, IsAdminRole
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_spectacular.utils import extend_schema


@extend_schema(
    description="List of products",
    tags=["Products"],
)
class ProductAPIView(generics.ListCreateAPIView):
    permission_classes = [IsSellerOrReadOnly]
    serializer_class = ProductWriteSerializer
    parser_classes = (MultiPartParser, FormParser)

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

    def perform_create(self, serializer):
        user = JWTAuthentication().authenticate(self.request)[0]

        # access_token = self.request.COOKIES.get("access_token")
        # user = JWTAuthentication().get_user(access_token)
        serializer.save(created_by=user)


@extend_schema(
    description="Product details",
    tags=["Products"],
)
class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailsSerializer
    permission_classes = [IsSellerOrReadOnly]


@extend_schema(
    description="Category List",
    tags=["Product Category"],
)
class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminRole]


@extend_schema(
    description="Product category details",
    tags=["Product Category"],
)
class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminRole]
    lookup_field = "slug"
