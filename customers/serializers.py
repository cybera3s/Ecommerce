from rest_framework import serializers

from customers.models import Address, Customer


class AddressSerializer(serializers.ModelSerializer):
    customer = serializers.HyperlinkedRelatedField(view_name='customers:customer-detail', read_only=True)
    url = serializers.HyperlinkedRelatedField(view_name='customers:address-detail', read_only=True)

    class Meta:
        model = Address
        fields = ['url', 'customer', 'state', 'city', 'postal_code', 'address_detail']


class CustomerSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Customer
        fields = ('id', 'user', 'gender')
