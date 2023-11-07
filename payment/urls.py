from django.urls import path
from .views import (
    CreateCheckOutSession,
    GuestCreateCheckoutSession,
    WebHook,
    stripe_webhook_view,
)
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("stripe-webhook/", stripe_webhook_view, name="stripe-webhook"),
    path(
        "create-checkout-session/",
        csrf_exempt(CreateCheckOutSession.as_view()),
        name="checkout_session",
    ),
    path(
        "guest-checkout/",
        GuestCreateCheckoutSession.as_view(),
        name="guest-user-checkout",
    ),
    path("webhook-test/", WebHook.as_view()),
]
