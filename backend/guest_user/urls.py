from django.urls import path
from .views import CartAPIView, PlaceOrderAPIView

urlpatterns = [
    path("guest_cart/", CartAPIView.as_view(), name="guest-cart-api"),
    path("place-order/", PlaceOrderAPIView.as_view(), name="place_order"),
]
