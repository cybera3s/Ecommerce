from django.contrib import admin
from .models import Customer, Address


class AddressInline(admin.StackedInline):
    model = Address
    fields = ('state', 'city', 'postal_code', 'address_detail', 'customer')
    extra = 1


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender')
    inlines = [AddressInline]
    raw_id_fields = ('user',)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    fields = ('state', 'city', 'postal_code', 'address_detail', 'customer')
    list_display = ('state', 'city', 'customer')
    search_fields = ('state', 'city', 'customer')
    list_filter = ('last_updated',)
