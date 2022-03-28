from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets
from product.models import Product, Brand
from .serializers import ProductSerializer, BrandSerializer


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [IsSuperuserPermission]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'discount', 'brand']
    search_fields = ['name', 'brand__name']
    ordering_fields = '__all__'


class BrandViewSet(viewsets.ModelViewSet):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name', 'country']
    search_fields = ['name', 'country']
    ordering_fields = '__all__'
