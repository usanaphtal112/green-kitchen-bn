# Generated by Django 4.2.1 on 2023-06-22 18:10

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("order", "0002_remove_orderitem_price_alter_orderitem_product_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Orderproduct",
            new_name="Order",
        ),
    ]