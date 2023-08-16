# Generated by Django 4.2.1 on 2023-08-02 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0007_alter_product_image'),
        ('guest_user', '0004_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Guest_Order',
            new_name='GuestOrder',
        ),
        migrations.RenameModel(
            old_name='Guest_OrderItem',
            new_name='GuestOrderItem',
        ),
        migrations.RenameField(
            model_name='guestorder',
            old_name='phone_numbe',
            new_name='phone_number',
        ),
        migrations.RenameIndex(
            model_name='guestorder',
            new_name='guest_user__created_e29ad6_idx',
            old_name='guest_user__created_a6a93c_idx',
        ),
    ]
