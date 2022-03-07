import json
from product.models import Category, Product


def access_category_items(request):
    """
      The context processor to access categories in all pages
    """
    categories = Category.objects.all()
    return {'nav_categories': categories}


def cart_items(request):
    products = []
    total_price = 0
    cart_items_count = 0   # for cart item count of cart icon in all pages

    if 'cart' in request.COOKIES:

        cart = json.loads(request.COOKIES['cart'])

        for p in cart.keys():
            product = Product.objects.get(id=p)
            products.append((product, cart[p]))
            total_price += int(cart[p]) * product.final_price

        cart_items_count = len(cart)

    return {'cart_item_count': cart_items_count, 'cart_products': products, 'cart_total_price': total_price}
