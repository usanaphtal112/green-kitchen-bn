from django.shortcuts import redirect
from django.urls import reverse
from cart.models import Cart
from django.http import JsonResponse


class CartMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            try:
                cart = Cart.objects.get(user=request.user)
                request.cart = cart
            except Cart.DoesNotExist:
                return JsonResponse(
                    {"error": "No product selected into Cart."}, status=400
                )

        response = self.get_response(request)
        return response
