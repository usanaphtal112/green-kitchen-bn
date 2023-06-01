# Generated by Django 4.2.1 on 2023-06-01 17:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_remove_user_username"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[("buyer", "Buyer"), ("seller", "Seller"), ("admin", "Admin")],
                default="buyer",
                max_length=20,
            ),
        ),
    ]
