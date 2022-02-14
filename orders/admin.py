from django.contrib import admin
from .models import Cart, OffCode, CartItem


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('customer', 'final_price',)
    search_fields = ('customer',)
    list_filter = ('created',)
    raw_id_fields = ('customer', 'off_code')


@admin.register(OffCode)
class OffCodeAdmin(admin.ModelAdmin):
    list_display = ('value', 'type',)
    search_fields = ('value', 'type')
    list_filter = ('created',)
