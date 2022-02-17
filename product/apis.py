# from rest_framework import status, generics
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
from .serializers import ProductSerializer
from product.models import Product
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView


class ProductListCreateApiView(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
