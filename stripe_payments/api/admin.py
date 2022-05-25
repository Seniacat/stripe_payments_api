from django.contrib import admin

from .models import Item, Order


class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description',
        'price'
    )
    search_fields = ('name', 'price')


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'customer',
        'orderitems',
        'discounts',
        'date_created',
        'date_completed',
        'amount_total'
    )
    search_fields = ('customer', 'price')


admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)