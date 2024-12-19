from django.contrib import admin

from shop.models import (
    Product,
    Order,
)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'buyer_email',
    )