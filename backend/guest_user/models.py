from django.db import models

from shops.models import Product


class GuestOrder(models.Model):
    PAYMENT_METHOD_CHOICES = (
        ("MTN", "MTN"),
        ("Card", "Card"),
        ("Airtel", "Airtel"),
        ("Cash", "Cash"),
    )
    full_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=10)
    district = models.CharField(max_length=50)
    sector = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    payment_method = models.CharField(
        max_length=200,
        choices=PAYMENT_METHOD_CHOICES,
        default="MTN",
    )
    message = models.TextField(default="No recommendation about the products")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["-created_at"]),
        ]

    def __str__(self):
        return f"Guest Order {self.id}"

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class GuestOrderItem(models.Model):
    guest_order = models.ForeignKey(
        GuestOrder, related_name="guest_orders", on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product, related_name="guest_order_items", on_delete=models.CASCADE
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
