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

