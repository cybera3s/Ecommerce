# from rest_framework import status, generics
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
from .serializers import ProductSerializer, BrandSerializer, CategorySerializer
from product.models import Product, Brand, Category
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, ListAPIView


class ProductListCreateApiView(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDetailApi(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class BrandListCreateApiView(ListCreateAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()


class CategoryListApiView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
