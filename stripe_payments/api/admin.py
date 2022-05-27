from django.contrib import admin

from .models import Coupon, Discount, Item, Order, OrderItem


class CouponAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'amount_off',
        'currency',
        'duration',
        'duration_in_months',
        'percent_off'
    )


class DiscountAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'customer',
        'date_end',
        'date_applied'
    )


class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description',
        'price',
        'currency'
    )
    search_fields = ('name', 'price')


class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        'order',
        'item',
        'quantity',
        'get_total_item_price'
    )
    search_fields = ('order__customer__username',)


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'customer',
        'date_created',
        'date_completed',
        'status',
        'get_total_price',
    )
    search_fields = (
        'customer__username',
        'price',
        'date_completed',
        'date_created'
    )


admin.site.register(Item, ItemAdmin)
admin.site.register(Coupon, CouponAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
