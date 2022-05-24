from django.contrib import admin
from .models import Cart, OffCode, CartItem


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('customer', 'final_price',)
    search_fields = ('customer',)
    list_filter = ('created',)
    raw_id_fields = ('customer', 'off_code')

    fieldsets = (
        ('pricing', {'fields': ['total_price', 'final_price', 'off_code', ]}),
        ('customer', {'fields': ['customer', 'address', ]})
    )
    readonly_fields = ('final_price', 'total_price')


@admin.register(OffCode)
class OffCodeAdmin(admin.ModelAdmin):
    fields = ('code', 'valid_from', 'valid_to', 'value', 'type', 'max_price', )
    list_display = ('code', 'value', 'type', 'active')
    search_fields = ('value', 'type')
    list_filter = ('created',)

    def active(self, obj):
        return obj.active

    active.boolean = True


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    fields = ('count', "cart", "product")
    list_display = ('product', 'count',)
    search_fields = ('product',)
    list_filter = ('cart',)
    raw_id_fields = ('cart', 'product')
