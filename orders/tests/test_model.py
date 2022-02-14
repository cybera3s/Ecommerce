from orders.models import Cart, CartItem, OffCode
from customers.models import Customer
from product.models import Product, Brand, Discount, Category
from django.test import TestCase
from datetime import datetime, timedelta
from django.utils.text import slugify


class CartTest(TestCase):
    def setUp(self) -> None:
        self.customer1 = Customer.objects.create_user('test1', 'test1@email.com', 'test1')
        self.off_code1 = OffCode.objects.create(value=10000, type='PRI', valid_from=datetime.now(),
                                                valid_to=datetime.now() + timedelta(days=5), code='abcd123465')
        self.cart1 = Cart(off_code=self.off_code1, customer=self.customer1)

        # brands
        self.brand1 = Brand.objects.create(name='LG', country='Japan')
        self.brand2 = Brand.objects.create(name='samsung', country='Korea')

        # categories
        self.category1 = Category.objects.create(name='Electrical')
        self.category2 = Category.objects.create(name='mobil', root=self.category1)

        # discounts
        self.discount1 = Discount.objects.create(value=2000, type='PRI')
        self.discount2 = Discount.objects.create(value=35, type='PER')

        # products
        self.product1 = Product.objects.create(name='TV', price=100000, description='some text', inventory=5,
                                               brand=self.brand1,
                                               category=self.category1, discount=self.discount1, slug='some-text')
        self.product2 = Product.objects.create(name='J5', price=200000, description='some text', inventory=10,
                                               brand=self.brand2,
                                               category=self.category2, slug='another-text')

        # cart items

        self.cart_item1 = CartItem.objects.create(cart=self.cart1, product=self.product1)
        self.cart_item2 = CartItem.objects.create(cart=self.cart1, product=self.product2)
