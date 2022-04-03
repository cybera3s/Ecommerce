import json
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status, authentication, permissions
from rest_framework.response import Response
from core.permissions import IsSuperuserPermission, CustomIsAuthenticatedOrReadOnly
from orders.models import Cart, CartItem
from orders.serializers import CartSerializer, CartItemSerializer
from rest_framework.views import APIView
from product.models import Product
from product.serializers import ProductSerializer
from utils.cart import Cart as CookieCart


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsSuperuserPermission]
    authentication_classes = [authentication.SessionAuthentication]


class CartItemApiView(APIView):
    serializer_class = CartItemSerializer
    cart = CookieCart
    permission_classes = [CustomIsAuthenticatedOrReadOnly]
    authentication_classes = [authentication.SessionAuthentication]

    def get(self, request, *args, **kwargs):
        cart_items = CartItem.objects.all()
        serializer = self.serializer_class(cart_items, many=True, context={'request': request})

        if 'pk' in kwargs:
            item = cart_items.filter(pk=kwargs['pk']).first()
            serializer = self.serializer_class(item)

        return Response(serializer.data)

    def post(self, request):
        data = {}
        serializer = self.serializer_class(data=request.data)
        cart = self.cart(request)
        product = Product.objects.get(pk=request.data.get('product'))
        data['product'] = ProductSerializer(product).data

        if serializer.is_valid():
            cart.add(product, serializer.validated_data['count'])

            if request.user.is_authenticated:  # add to cart for logged in users
                cart.merge_db_cart(request)
                db_cart, created = Cart.objects.get_or_create(customer=request.user.customer, is_active=True)
                serializer.validated_data['cart_id'] = db_cart.id
                serializer.save()

                cart.merge_db_cart(request)

                data.update({
                    'item': serializer.data,
                    'cart': cart.cart,
                    'auth': True
                })
                return Response(data, status=status.HTTP_201_CREATED)

            else:  # add to cart not logged in users

                data.update({
                    'item': serializer.data,
                    'cart': cart.cart,
                })
                response = Response(data, status=status.HTTP_201_CREATED)
                response.set_cookie('cart', json.dumps(cart.cart))  # register cart in cookies
                return response

        # Handle serializer Errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        cart = CookieCart(request)
        cart.merge_db_cart(request)

        try:

            item = get_object_or_404(CartItem, pk=pk)
            item.delete()
            cart.remove(item)
            return Response({'msg': 'delete successfully!', 'item': pk, 'total_price': cart.get_total_price(),
                             'items_count': len(cart)})

        except CartItem.DoesNotExist:
            return Response({'msg': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, *args, **kwargs):
        cart = CookieCart(request)
        cart.merge_db_cart(request)

        try:
            item = CartItem.objects.get(pk=request.data.get('item_id'))
        except CartItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        real_cart = Cart.objects.get(customer=request.user.customer, is_active=True)
        serializer = self.serializer_class(item, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            data = {
                'item': serializer.data,
                'cart_total_price': real_cart.total_worth(),
                'cart_final_price': real_cart.final_worth()
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
