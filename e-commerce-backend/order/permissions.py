from rest_framework.permissions import BasePermission
from .models import Order


class IsProductBuyer(BasePermission):
    message = "You must purchase the product to write a review."

    def has_permission(self, request, view):
        product_id = view.kwargs.get("product_id")
        current_user = request.user

        # Check if the user has a completed order with the product
        order_exists = Order.objects.filter(
            owner=current_user, status="Paid", items__product_id=product_id
        ).exists()
        return order_exists
