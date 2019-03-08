from django.contrib import admin
from orders.models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['content']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_no',
                    'name',
                    'phone',
                    'postal_code',
                    'address',
                    'extraAddress',
                    'detailAddress',
                    'paid',
                    'totalCost',
                    'created', 'updated']
    list_filter = ['order_no', 'paid', 'created', 'updated']
    inlines = [OrderItemInline]