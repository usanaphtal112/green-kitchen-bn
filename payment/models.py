from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model


class Payment(models.Model):
    cart_id = models.PositiveIntegerField()
    # user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    client_secret = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Payment #{self.id} - Cart ID: {self.cart_id}"
