from .models import Product, Brand
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    discount = serializers.StringRelatedField()
    category = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = (
            'name', 'price', 'description', 'picture', 'inventory', 'slug', 'created', 'last_updated', 'is_active',
            'brand',
            'discount', 'final_worth', 'category')
