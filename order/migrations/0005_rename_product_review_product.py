# Generated by Django 4.2.1 on 2023-06-28 11:30

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0004_alter_order_status_review"),
    ]

    operations = [
        migrations.RenameField(
            model_name="review",
            old_name="Product",
            new_name="product",
        ),
    ]
