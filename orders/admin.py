from django.contrib import admin
from orders.models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['content']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_no',
                    'imp_uid',
                    'name',
                    'phone',
                    'postal_code',
                    'address',
                    'extraAddress',
                    'detailAddress',
                    'method',
                    'paid',
                    'delivery_fee',
                    'delivery',
                    'totalCost',
                    'note',
                    'created', 'updated']
    list_filter = ['order_no',
                   'paid',
                   'created',
                   'updated']
    inlines = [OrderItemInline]