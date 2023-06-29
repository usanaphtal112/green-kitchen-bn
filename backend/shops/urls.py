from django.urls import path
from .views import (
    ProductAPIView,
    ProductDetailAPIView,
    CategoryListView,
    CategoryDetailView,
)

urlpatterns = [
    path("products/", ProductAPIView.as_view(), name="product-list"),
    path("products/<int:pk>/", ProductDetailAPIView.as_view(), name="product-detail"),
    path("categories/", CategoryListView.as_view(), name="category-list"),
    path(
        "categories/<slug:slug>/",
        CategoryDetailView.as_view(),
        name="category-detail",
    ),
]
