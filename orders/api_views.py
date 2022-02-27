from rest_framework import viewsets
from core.permissions import IsSuperuserPermission
from orders.models import Cart, CartItem
from orders.serializers import CartSerializer, CartItemSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsSuperuserPermission]


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsSuperuserPermission]
