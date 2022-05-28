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
        'coupon',
        'date_end',
        'date_applied'
    )
    search_fields = ('coupon__id', 'customer__username')


class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description',
        'price',
        'currency'
    )
    search_fields = ('name', 'price')


class OrderItemAdminInline(admin.TabularInline):
    model = OrderItem
    extra = 1


class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        'order',
        'item',
        'quantity',
        'get_total_item_price'
    )
    search_fields = ('order__customer__username',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemAdminInline,)
    list_display = (
        'id',
        'customer',
        'date_created',
        'date_completed',
        'status',
        'get_total_price'
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
