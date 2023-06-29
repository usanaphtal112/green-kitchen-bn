from django.urls import path
from .views import (
    OrderDetailsAPIView,
    UserOrdersAPIView,
    ReviewAPIView,
)


urlpatterns = [
    path("orders/", UserOrdersAPIView.as_view(), name="order-list"),
    path("orders/<int:order_id>/", OrderDetailsAPIView.as_view(), name="order-details"),
    path("review/<int:product_id>/", ReviewAPIView.as_view(), name="product-review"),
]
