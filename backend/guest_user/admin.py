from django.contrib import admin

# Register your models here.
from .models import GuestOrder, GuestOrderItem


class GuestOrderItemInline(admin.TabularInline):
    model = GuestOrderItem
    raw_id_fields = ["product"]


@admin.register(GuestOrder)
class GuestOrderAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "full_name",
        "phone_number",
        "district",
        "sector",
        "address",
        "paid",
        "created_at",
        "updated_at",
        "message",
    ]

    list_filter = ["paid", "created_at", "updated_at"]
    inlines = [GuestOrderItemInline]
