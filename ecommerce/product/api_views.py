from rest_framework import viewsets, authentication
from core.permissions import IsSuperuserPermission
from product.models import Product, Brand
from .serializers import ProductSerializer, BrandSerializer


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [IsSuperuserPermission]


class BrandViewSet(viewsets.ModelViewSet):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [IsSuperuserPermission]
