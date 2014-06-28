from django.contrib import admin
from orders.models import Stock, StatusOrders, Sales


class StockAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'price',
    ]


class StatusOrdersAdmin(admin.ModelAdmin):
    list_display = [
        'items',
        'amount',
        'date_and_time',
        'status',
        'waiter',
        'bartender',
    ]


class SalesAdmin(admin.ModelAdmin):
    list_display = [
        'items_sales',
        'count'
    ]

    def items_sales(self, instance):
        return instance.item.name

admin.site.register(Stock, StockAdmin)
admin.site.register(StatusOrders, StatusOrdersAdmin)
admin.site.register(Sales, SalesAdmin)
