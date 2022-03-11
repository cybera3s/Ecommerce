import json

from product.models import Product

CART_SESSION_COOKIE_ID = 'cart'


class Cart:
    def __init__(self, request):
        self.cookie = request.COOKIES
        cart = json.loads(self.cookie.get(CART_SESSION_COOKIE_ID)) if self.cookie.get(CART_SESSION_COOKIE_ID) else None

        if not cart:
            cart = {}
        self.cart = cart

    def add(self, product, count):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'count': 0, 'price': str(product.final_worth)}
        self.cart[product_id]['count'] += count

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['total_price'] = int(item['price']) * item['quantity']
            yield item

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def get_total_price(self):
        return sum(int(item['price']) * item['quantity'] for item in self.cart.values())

    def __len__(self):
        return sum(item['count'] for item in self.cart.values())
