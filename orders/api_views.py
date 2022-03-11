import json
from rest_framework import viewsets, status
from rest_framework.response import Response
from core.permissions import IsSuperuserPermission
from orders.models import Cart, CartItem
from orders.serializers import CartSerializer, CartItemSerializer
from rest_framework.views import APIView
from product.models import Product
from product.serializers import ProductSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsSuperuserPermission]


#
# class CartItemViewSet(viewsets.ModelViewSet):
#     queryset = CartItem.objects.all()
#     serializer_class = CartItemSerializer
#     permission_classes = [IsSuperuserPermission]


# def get_create_cart_cookie(request):
#     if 'cart' in request.COOKIES:
#         cookie_cart = json.loads(request.COOKIES['cart'])
#         customer_cart = Cart.objects.get_or_create(customer=request.user.customer)
#
#         customer_cart_items = customer_cart.items.all()
#
#         for item in customer_cart_items:
#             if item in cookie_cart:
#                 item.count = cookie_cart[item.id]  # merging existence cart with new cart in cookies
#             else:
#                 new_item = CartItem(product_id=item, count=cookie_cart[item], cart=customer_cart)
#                 customer_cart_items.add(new_item)
#
#         request.session['cart'] = customer_cart
#         return True
#
#     # if cart is not in cookies
#     return False
class CartItemApiView(APIView):
    serializer_class = CartItemSerializer

    def get(self, request):
        cart_items = CartItem.objects.all()
        serializer = self.serializer_class(cart_items, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        from core.utils.cart import Cart
        serializer = self.serializer_class(data=request.data)
        cart = Cart(request)
        product = Product.objects.get(pk=request.data.get('product'))

        if serializer.is_valid():
            cart.add(product, serializer.validated_data['count'])
            data = {
                'item': serializer.data,
                'cart': cart.cart,
                'product': ProductSerializer(product).data
            }
            response = Response(data, status=status.HTTP_201_CREATED)
            response.set_cookie('cart', json.dumps(cart.cart))
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # from core.utils.cart import Cart
        # data = request.POST
        # product_id, count = data['product'], data['count']

        # cart = Cart(request)
        # if request.user.is_authenticated:
        #
        #     customer_cart, created = Cart.objects.get_or_create(customer=request.user.customer)
        #     cookie_cart = get_cart_cookies(request)
        #     customer_cart_items = customer_cart.items.all()
        #     data = {
        #         'product': product_id,
        #         'count': count,
        #         'cart': customer_cart.id
        #     }
        #
        #     if cookie_cart:
        #         for item in cookie_cart:
        #             order_item = CartItem.objects.get(product_id=item)
        #             if order_item:
        #                 order_item.count += int(cookie_cart[item])
        #                 order_item.save()
        #             else:
        #                 CartItem.objects.create(product_id=item, count=cookie_cart[item], cart=customer_cart)
        #
        #     if int(product_id) in customer_cart_items.values_list('product', flat=True):
        #         item = CartItem.objects.get(product_id=product_id)
        #         item.count += int(count)
        #         item.save()
        #     else:
        #         serializer = self.serializer_class(data=data)
        #         if serializer.is_valid():
        #             serializer.save()
        #
        #     serialized_products = []
        #
        #     for p in customer_cart_items:  # serialize products in cart
        #         product = Product.objects.get(id=p.product.id)
        #         serialized_product = ProductSerializer(product).data
        #         serialized_products.append(serialized_product)
        #
        #     data = {
        #         'cart': dict(list(customer_cart_items.values_list('product', 'count'))),
        #         'products': serialized_products
        #     }
        #     request.session['cart'] = data['cart']
        #     response = JsonResponse(data)
        #     response.delete_cookie('cart')
        #     return response
        #
        # # user is not logged in
        # else:

        # cart = {
        #     product_id: count,
        # }

        # if 'cart' in request.COOKIES:
        #     cart = json.loads(request.COOKIES['cart'])

        # check if product already exists in cart
        # if product_id in cart:
        #     cart[product_id], count = int(cart[product_id]), int(count)
        #     cart[product_id] += count
        # else:
        #     cart[product_id] = count

        # if cart is not in cookies
        # serialized_products = []
        #
        # for p in cart.keys():  # serialize products in cart
        #     product = Product.objects.get(id=p)
        #     serialized_product = ProductSerializer(product).data
        #     serialized_products.append(serialized_product)

        # data = {
        #     'cart': cart,
        #     'products': serialized_products
        # }

        # response =   # send data as post response
        # response.set_cookie('cart', json.dumps(cart))
        #     return response

#
# class CartItemApi(APIView):
#     serializer_class = CartItemSerializer
#
#     def get(self, request, order_id=None):
#         items = CartItem.objects.all()
#         if order_id:
#             items = items.filter(cart_id=order_id)
#
#         if not items:
#             return Response({'msg': 'empty'})
# #
#         serializer = self.serializer_class(items, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = self.serializer_class(request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
