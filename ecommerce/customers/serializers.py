from rest_framework import serializers

from customers.models import Address, Customer


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ['customer', 'state', 'city', 'postal_code', 'address_detail']


class CustomerSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Customer
        fields = ('id', 'user', 'gender')
