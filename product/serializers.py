from .models import Product, Brand, Category, Picture
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    discount = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    images = serializers.StringRelatedField(source='pictures', many=True, read_only=True)

    class Meta:
        model = Product
        fields = (
            'id', 'name', 'price', 'description', 'inventory', 'slug', 'created', 'last_updated',
            'is_active', 'brand', 'discount', 'final_worth', 'category', 'images')


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    root = serializers.StringRelatedField()
    discount = serializers.StringRelatedField()

    class Meta:
        model = Category
        fields = ('name', 'root', 'discount')
