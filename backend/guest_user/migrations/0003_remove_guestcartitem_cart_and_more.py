# Generated by Django 4.2.1 on 2023-07-16 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guest_user', '0002_guestcartitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guestcartitem',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='guestcartitem',
            name='product',
        ),
        migrations.DeleteModel(
            name='GuestCart',
        ),
        migrations.DeleteModel(
            name='GuestCartItem',
        ),
    ]
