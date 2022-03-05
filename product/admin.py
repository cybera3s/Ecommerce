from django.contrib import admin
from .models import Product, Brand, Category, Discount, Picture


class PictureInline(admin.StackedInline):
    model = Picture
    fields = ('picture', 'product')
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'final_worth', 'is_available')
    search_fields = ('name', 'category', 'brand')
    list_filter = ('inventory',)
    raw_id_fields = ('brand', 'discount', 'category')
    fieldsets = (
        ('information', {'fields': ['name', 'price', 'description', 'brand', 'category', 'final_worth', 'slug', ]}),
        ('specific', {'fields': ['discount', 'inventory',]})
    )
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('final_worth',)
    inlines = [PictureInline]


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    list_display_links = ('name',)
    search_fields = ('name', 'country')
    list_filter = ('name', 'country')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'root')
    search_fields = ('name',)
    list_filter = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('value', 'type')
    search_fields = ('value',)


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    fields = ('picture', 'product')
    list_display = ('picture', 'product')
