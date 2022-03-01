# from rest_framework import status, generics
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, ListAPIView
from rest_framework import viewsets

from product.models import Product, Brand, Category
from .serializers import ProductSerializer, BrandSerializer, CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'discount', 'brand']
    search_fields = ['name', ]
    ordering_fields = '__all__'


class ProductDetailApi(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class BrandListCreateApiView(ListCreateAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()


class CategoryListApiView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
