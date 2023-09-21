# Generated by Django 4.2.1 on 2023-06-22 18:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("shops", "0006_delete_product_order"),
        ("order", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="orderitem",
            name="price",
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="shops.product"
            ),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="quantity",
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.CreateModel(
            name="Orderproduct",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("placed_at", models.DateTimeField(auto_now_add=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Paid", "Paid"),
                            ("Pending", "Pending"),
                            ("Failed", "Failed"),
                        ],
                        default="Pending",
                        max_length=10,
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="items",
                to="order.orderproduct",
            ),
        ),
        migrations.DeleteModel(
            name="Order",
        ),
    ]