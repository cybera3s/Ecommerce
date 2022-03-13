import json

from orders.models import CartItem
from product.models import Product

CART_SESSION_COOKIE_ID = 'cart'


class Cart:
    def __init__(self, request):
        self.cookie = request.COOKIES
        cart = json.loads(self.cookie.get(CART_SESSION_COOKIE_ID)) if self.cookie.get(CART_SESSION_COOKIE_ID) else None
        # if there is no cart in cookies creates it
        if not cart:
            cart = {}
        self.cart = cart
        self.is_registered_in_db = False

    def add(self, product, count):
        print('adding: ', self.cart)
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
            item['total_price'] = int(item['price']) * item['count']
            yield item

    def merge_db_cart(self, request):
        from orders.models import Cart as db_cart

        if request.user.is_authenticated:
            real_cart, created = db_cart.objects.get_or_create(customer=request.user.customer)
            items = real_cart.items.all()
            if items:
                for item in items:
                    self.cart[str(item.product.id)] = {'count': item.count, 'price': item.product.final_worth}
            else:
                print('cart in db is empty!')

    def register_in_db(self, request):
        from orders.models import Cart as db_cart
        if not request.user.is_authenticated:
            print('there is no logged in users!')
            return False
        real_cart, created = db_cart.objects.get_or_create(customer=request.user.customer)
        items = real_cart.items.all()
        item_ids = items.values_list('product', flat=True)
        cart = self.cart
        print('cart copy in cookie: ', cart)
        if cart:
            for i in cart:
                if int(i) not in item_ids:
                    CartItem.objects.create(count=cart[i].get('count'), product_id=int(i), cart=real_cart)
                else:
                    p = CartItem.objects.get(product__id=int(i))
                    p.count += cart[i].get('count')
                    p.save()

            print(f'#{len(self.cart)} items successfully registered in db')
            self.is_registered_in_db = True

        else:
            print('there is no items in cookies!')

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def get_total_price(self):
        return sum(int(item['price']) * item['count'] for item in self.cart.values())

    def __len__(self):
        return len(self.cart)

    def __str__(self):
        return self.cart.cart
