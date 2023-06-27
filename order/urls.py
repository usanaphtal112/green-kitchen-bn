from django.urls import path
from .views import (
    OrderDetailsAPIView,
    UserOrdersAPIView,
)


urlpatterns = [
    path("orders/", UserOrdersAPIView.as_view(), name="order-list"),
    path("orders/<int:order_id>/", OrderDetailsAPIView.as_view(), name="order-details"),
]
