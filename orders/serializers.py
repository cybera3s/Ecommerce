from rest_framework import serializers

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
        fields = ('id', 'count', 'cart', 'product')
        extra_kwargs = {'cart': {'required': False}}

    def validate_count(self, value):
        """
        Check that the count be between 1 to corresponding product inventory
        """
        product_id = self.instance.product.id if self.partial else self.initial_data.get('product')

        product = Product.objects.get(pk=product_id)

        if value > product.inventory:
            raise serializers.ValidationError(_("Maximum count is ") + str(product.inventory))
            
        if value < 1:
            raise serializers.ValidationError(_("Minimum count is 1"))

        return value

    def save(self, **kwargs):
        """
        overwrites count of repetitious items  otherwise normal save
        """
        if not self.partial:
            p = self.validated_data['product']
            item_product = CartItem.objects.filter(product=p)
            if item_product.exists():
                item = item_product.first()
                item.count += self.validated_data['count']
                item.save()
            else:
                return super().save(**kwargs)
        else:
            return super().save(**kwargs)

    # Second method for using model validate
    # def validate(self, attrs):
    #     instance = CartItem(**attrs)
    #     instance.clean()
    #     return attrs
    # if value > product.inventory:
    #     raise serializers.ValidationError(f'Maximum count is {product.inventory}')
    # return value
