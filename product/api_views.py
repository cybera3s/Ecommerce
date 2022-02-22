# from rest_framework import status, generics
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
from .serializers import ProductSerializer, BrandSerializer
from product.models import Product, Brand
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView


class ProductListCreateApiView(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDetailApi(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class BrandListCreateApiView(ListCreateAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()