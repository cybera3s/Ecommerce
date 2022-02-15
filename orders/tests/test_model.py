from orders.models import Cart, CartItem, OffCode
from customers.models import Customer
from product.models import Product, Brand, Discount, Category
from django.test import TestCase
from datetime import timedelta
from django.utils import timezone


class CartTest(TestCase):
    def setUp(self) -> None:
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

        # Cart requirements
        self.customer1 = Customer.objects.create_user('test1', 'test1@email.com', 'test1', gender=1,
                                                      phone_number='09224023292')
        self.off_code1 = OffCode.objects.create(value=10000, type='PRI', code='123465', valid_from=timezone.now(),
                                                valid_to=timezone.now() + timedelta(days=5))
        self.cart1 = Cart.objects.create(customer=self.customer1, off_code=self.off_code1)

        # cart items

        self.cart_item1 = CartItem.objects.create(cart=self.cart1, product=self.product1)
        self.cart_item2 = CartItem.objects.create(cart=self.cart1, product=self.product2)

    def test1_total_worth_success(self):
        total_price = self.cart1.total_worth()
        sum_item_prices = self.cart_item1.product.final_price + self.cart_item2.product.final_price

        self.assertGreater(total_price, 0)
        self.assertEqual(total_price, sum_item_prices)

    def test2_final_worth_success(self):
        total_price = self.cart1.total_worth()

        self.assertLess(self.cart1.final_worth(), total_price)
        self.assertEqual(self.cart1.final_worth(), total_price - self.off_code1.profit_value(total_price))