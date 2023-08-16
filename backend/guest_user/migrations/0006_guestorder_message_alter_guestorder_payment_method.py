# Generated by Django 4.2.1 on 2023-08-04 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest_user', '0005_rename_guest_order_guestorder_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='guestorder',
            name='message',
            field=models.TextField(default='No recommendation about the products'),
        ),
        migrations.AlterField(
            model_name='guestorder',
            name='payment_method',
            field=models.CharField(choices=[('MTN', 'MTN'), ('Card', 'Card'), ('Airtel', 'Airtel'), ('Cash', 'Cash')], default='MTN', max_length=200),
        ),
    ]
