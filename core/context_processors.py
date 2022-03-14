from product.models import Category
from utils.cart import Cart


def access_category_items(request):
    """
      The context processor to access categories in all pages
    """
    categories = Category.objects.all()
    return {'nav_categories': categories}


#
# def get_cart_cookies(request):
#     if 'cart' in request.COOKIES:
#         cookie_cart = json.loads(request.COOKIES['cart'])
#         return cookie_cart
#     return {}

#
# def cart_items(request):
#     products = []
#     total_price = 0
#     cart_items_count = 0  # for cart item count of cart icon in all pages
#     cookie_cart = get_cart_cookies(request)
#
#     if request.user.is_authenticated:
#         cart = Cart.objects.get(customer=request.user.customer)
#         items = cart.items.all()
#
#
#         if cookie_cart:
#             for item in cookie_cart:
#                 try:
#                     order_item = CartItem.objects.get(product_id=item)
#                     order_item.count += int(cookie_cart[item])
#                     order_item.save()
#                 except:
#                     CartItem.objects.create(product_id=item, count=cookie_cart[item], cart=cart)
#
#             request.COOKIES.pop('cart')
#
#         products = []
#
#         for i in items:
#             product = i.product
#             products.append((product, i.count))
#
#         total_price = cart.final_worth()
#         cart_items_count = len(items)
#
#         return {'cart_item_count': cart_items_count, 'cart_products': products, 'cart_total_price': total_price}
#
#     if cookie_cart:
#         for p in cookie_cart.keys():
#             product = Product.objects.get(id=p)
#             products.append((product, cookie_cart[p]))
#             total_price += int(cookie_cart[p]) * product.final_price
#
#         cart_items_count = len(cookie_cart)
#
#     return {'cart_item_count': cart_items_count, 'cart_products': products, 'cart_total_price': total_price}

def cart(request):
    active_cart = Cart(request)

    # if request.user.is_authenticated and hasattr(request.user, 'customer'):
    #     active_cart.merge_db_cart(request)
    print('in context context processor : ', active_cart.cart)

    return {
        'cart': active_cart
    }
