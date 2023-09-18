from django.urls import path
from .views import (
    ProductAPIView,
    ProductDetailAPIView,
    CategoryListView,
    CategoryDetailView,
    ProductByCategoryListView,
    ProductByUserListView,
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
    path(
        "products/category/<slug:category_slug>/", ProductByCategoryListView.as_view()
    ),
    path("products/users/<int:user_id>/", ProductByUserListView.as_view()),
]
