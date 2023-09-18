from rest_framework import permissions
from .models import Product
from rest_framework.exceptions import PermissionDenied


class IsSellerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            # Allow all safe methods (GET, HEAD, OPTIONS)
            return True
        elif request.method == "POST":
            # Only allow authenticated sellers to create a new product
            if not request.user.is_authenticated:
                raise PermissionDenied("You must be authenticated to create a product.")
            return request.user.role == "seller"
        else:
            # For all other unsafe methods (PUT, PATCH, DELETE)
            # Check if the product is created by the current logged-in user
            product_id = view.kwargs.get("pk")
            product = Product.objects.get(pk=product_id)
            if not request.user.is_authenticated:
                raise PermissionDenied(
                    "You must be authenticated to perform this action."
                )
            return product.created_by == request.user and request.user.role == "seller"


class IsAdminRole(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "admin"


class IsBuyerRoleOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "buyer"
