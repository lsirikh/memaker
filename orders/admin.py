from django.contrib import admin
from orders.models import Order, OrderItem, OrderCancel, OrderDelivery, ImportInfo

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = [
        'content',
    ]

class ImportInfoAdmin(admin.ModelAdmin):
    list_display = [
        'amount',
        'apply_num',
        'bank_code',
        'bank_name',
        'buyer_addr',
        'buyer_email',
        'buyer_name',
        'buyer_postcode',
        'buyer_tel',
        'cancel_amount',
        'cancel_history',
        'cancel_reason',
        'cancel_receipt_urls',
        'cancelled_at',
        'card_code',
        'card_name',
        'card_quota',
        'cash_receipt_issued',
        'channel',
        'currency',
        'custom_data',
        'escrow',
        'fail_reason',
        'failed_at',
        'imp_uid',
        'merchant_uid',
        'name',
        'paid_at',
        'pay_method',
        'pg_id',
        'pg_provider',
        'pg_tid',
        'receipt_url',
        'status',
        'user_agent',
        'vbank_code',
        'vbank_date',
        'vbank_holder',
        'vbank_issued_at',
        'vbank_name',
        'vbank_num',
    ]

admin.site.register(ImportInfo, ImportInfoAdmin)

class OrderDeliveryAdmin(admin.ModelAdmin):
    list_display = [
        'delivery_fee',
        'delivery_status',
        'delivery_agent',
        'delivery_code',
        'delivery_note',
        'name',
        'email',
        'phone',
        'postal_code',
        'address',
        'detailAddress',
        'extraAddress',

    ]


admin.site.register(OrderDelivery, OrderDeliveryAdmin)

class OrderDeliveryInline(admin.StackedInline):
    model = OrderDelivery
    fields = [
        'delivery_fee',
        'delivery_status',
        'delivery_agent',
        'delivery_code',
        'delivery_note',
        'name',
        'email',
        'phone',
        'postal_code',
        'address',
        'detailAddress',
        'extraAddress',
    ]
    list_editable = [
        'delivery_fee',
        'delivery_status',
        'delivery_agent',
        'delivery_code',
        'delivery_note',
        'name',
        'email',
        'phone',
        'postal_code',
        'address',
        'detailAddress',
        'extraAddress',
    ]

class OrderCacelAdmin(admin.ModelAdmin):
    list_display = [
        'merchant_uid',
        'note',
        'created'
    ]

admin.site.register(OrderCancel, OrderCacelAdmin)

class OrderCancelInline(admin.TabularInline):
    model = OrderCancel
    fields = [
        'merchant_uid',
        'note',
    ]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
                    'merchant_uid',
                    'imp_uid',
                    'confirm',
                    # 'method',
                    # 'paid',
                    # 'delivery_fee',
                    # 'delivery',
                    'isDirect',
                    'totalCost',
                    'tex_free_cost',
                    # 'note',
                    # 'name',
                    # 'phone',
                    # 'postal_code',
                    # 'address',
                    # 'extraAddress',
                    # 'detailAddress',
                    'created',
                    'updated'
                    ]
    list_editable = [
                    'confirm',
                    # 'method',
                    # 'paid',
                    # 'delivery_fee',
                    # 'delivery',
                    # 'note',
                    # 'name',
                    # 'phone',
                    # 'postal_code',
                    # 'address',
                    # 'extraAddress',
                    # 'detailAddress',
                    ]
    list_filter = [
                    # 'order_no',
                    # 'paid',
                    # 'created',
                    # 'updated'
                    ]
    inlines = [
                OrderItemInline,
                OrderCancelInline,
                OrderDeliveryInline]