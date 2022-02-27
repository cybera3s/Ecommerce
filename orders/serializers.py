from rest_framework import serializers

from orders.models import Cart, CartItem


class CartSerializer(serializers.HyperlinkedModelSerializer):
    customer = serializers.HyperlinkedRelatedField(view_name='customers:customer-detail', read_only=True)
    address = serializers.HyperlinkedRelatedField(view_name='customers:address-detail', read_only=True)
    items = serializers.HyperlinkedRelatedField(view_name='orders:cartitem-detail', queryset=CartItem.objects.all(), many=True)

    class Meta:
        model = Cart
        fields = ('customer', 'address', 'final_price', 'items')


class CartItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'
