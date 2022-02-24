# from rest_framework import status, generics
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
from .serializers import AddressSerializer, CustomerSerializer
from customers.models import *
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, ListAPIView
from rest_framework import permissions


class CustomerListApiView(ListCreateAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

#
# class ProductDetailApi(RetrieveUpdateDestroyAPIView):
#     serializer_class = ProductSerializer
#     queryset = Product.objects.all()
#
#
# class BrandListCreateApiView(ListCreateAPIView):
#     serializer_class = BrandSerializer
#     queryset = Brand.objects.all()
#
#
# class CategoryListApiView(ListAPIView):
#     serializer_class = CategorySerializer
#     queryset = Category.objects.all()
