from django.contrib import admin
from .models import Product, Brand, Category, Discount


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    search_fields = ('name', 'category', 'brand')
    list_filter = ('inventory',)
    raw_id_fields = ('brand', 'discount', 'category')
    fieldsets = (
        ('information',
         {'fields': ['name', 'price', 'description', 'brand', 'category']}),
        ('Specifications',
         {'fields': ['discount', 'inventory', 'slug', 'picture']})
    )
