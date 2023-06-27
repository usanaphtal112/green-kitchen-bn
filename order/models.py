from django.db import models
from django.conf import settings
from shops.models import Product


class Order(models.Model):
    PAYMENT_STATUS_CHOICES = (
        ("Paid", "Paid"),
        ("Pending", "Pending"),
        ("Failed", "Failed"),
        ("Cancelled", "Cancelled"),
    )

    placed_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=10,
        choices=PAYMENT_STATUS_CHOICES,
        default="Pending",
    )

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self):
        return f"Order #{self.id} - {self.status}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.product.name} (Qty: {self.quantity})"
