from rest_framework import viewsets
from .permissions import IsSuperuserPermission, IsOwnerPermission
from .serializers import AddressSerializer, CustomerSerializer
from customers.models import *
from rest_framework import authentication


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    permission_classes = [IsSuperuserPermission]
    authentication_classes = [authentication.BasicAuthentication]


class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    permission_classes = [IsOwnerPermission]
    authentication_classes = [authentication.BasicAuthentication]

    def get_queryset(self):
        user = self.request.user
        return Address.objects.filter(customer__user=user)
