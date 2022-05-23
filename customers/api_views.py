from rest_framework import viewsets, status
from rest_framework.response import Response

from core.permissions import IsSuperuserPermission, IsOwnerPermission
from .serializers import AddressSerializer, CustomerSerializer
from customers.models import *
from rest_framework import authentication


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    permission_classes = [IsSuperuserPermission]
    authentication_classes = [authentication.SessionAuthentication]


class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    permission_classes = [IsOwnerPermission]
    authentication_classes = [authentication.SessionAuthentication]

    def get_queryset(self):
        user = self.request.user
        return Address.objects.filter(customer__user=user)

    def destroy(self, request, *args, **kwargs):
        address = self.get_object()
        try:
            address.delete()
        except Exception:
            return Response({'msg': 'Address in use!'}, status=status.HTTP_403_FORBIDDEN)

        return Response(status=status.HTTP_204_NO_CONTENT)