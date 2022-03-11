from rest_framework import serializers

import product
from orders.models import Cart, CartItem
from product.models import Product
from django.utils.translation import gettext_lazy as _

class CartSerializer(serializers.HyperlinkedModelSerializer):
    customer = serializers.HyperlinkedRelatedField(view_name='customers:customer-detail', read_only=True)
    address = serializers.HyperlinkedRelatedField(view_name='customers:address-detail', read_only=True)
    items = serializers.HyperlinkedRelatedField(view_name='orders:cartitem-detail', queryset=CartItem.objects.all(),
                                                many=True)

    class Meta:
        model = Cart
        fields = ('customer', 'address', 'final_price', 'items')


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ('count', 'cart', 'product')
        extra_kwargs = {'cart': {'required': False}}

    def validate_count(self, value):
        """
        Check that the count be between 1 to corresponding product inventory
        """
        product_id = self.initial_data.get('product')
        product = Product.objects.get(pk=product_id)
        if value < 1:
            raise serializers.ValidationError(_("Minimum count is 1"))

        if value > product.inventory:
            raise serializers.ValidationError(_("Maximum count is {}").format(product.inventory))

        return value
    # Second method for using model validate
    # def validate(self, attrs):
    #     instance = CartItem(**attrs)
    #     instance.clean()
    #     return attrs
        # if value > product.inventory:
        #     raise serializers.ValidationError(f'Maximum count is {product.inventory}')
        # return value
