from django.contrib import admin
from cart.models import Cart
# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'user',
        'content',
        'cost',
        'quantity',
        'get_total',
        'created_at',
        'updated_at'
    ]

    def get_total(self, obj):
        return obj.get_cost()

admin.site.register(Cart, CartAdmin)
