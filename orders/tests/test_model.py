from core.models import User
from orders.models import Cart, CartItem, OffCode
from customers.models import Customer, Address
from product.models import Product, Brand, Discount, Category
from django.test import TestCase
from datetime import timedelta
from django.utils import timezone


class CartTest(TestCase):
    def setUp(self) -> None:
        # brands
        self.brand1 = Brand.objects.create(name='LG', country='Japan')
        self.brand2 = Brand.objects.create(name='samsung', country='Korea')
        self.brand3 = Brand.objects.create(name='Lenovo', country='China')

        # categories
        self.category1 = Category.objects.create(name='Electrical')
        self.category2 = Category.objects.create(name='mobile', root=self.category1)
        self.category3 = Category.objects.create(name='Laptop', root=self.category1)

        # discounts
        self.discount1 = Discount.objects.create(value=2000, type='PRI')
        self.discount2 = Discount.objects.create(value=35, type='PER')

        self.off_code1 = OffCode.objects.create(value=10000, type='PRI', code='123465', valid_from=timezone.now(),
                                                valid_to=timezone.now() + timedelta(days=5))
        self.off_code2 = OffCode.objects.create(value=20, type='PER', code='abed', valid_from=timezone.now(),
                                                valid_to=timezone.now() + timedelta(days=2))
        # products
        self.product1 = Product.objects.create(name='TV', price=100000, description='some text', inventory=5,
                                               brand=self.brand1,
                                               category=self.category1, discount=self.discount1, slug='some-text')
        self.product2 = Product.objects.create(name='J5', price=200000, description='some text', inventory=10,
                                               brand=self.brand2,
                                               category=self.category2, slug='another-text')

        self.product3 = Product.objects.create(name='a51', price=10000, description='a51', inventory=5,
                                               brand=self.brand2,
                                               category=self.category2, slug='another-text')
        self.product4 = Product.objects.create(name='Z-book', price=10000, description='Z-book', inventory=5,
                                               brand=self.brand3,
                                               category=self.category3, slug='another-text')
        # customers
        self.user1 = User.objects.create_user(email='test1@email.com', phone='09224023292', password='1234')
        self.customer1 = Customer.objects.create(gender=1, user=self.user1)

        self.user2 = User.objects.create_user(email='test2@email.com', phone='09123456789', password='1234')
        self.customer2 = Customer.objects.create(gender=1, user=self.user2)
        # addresses
        self.address1 = Address.objects.create(state='Tehran', city='Tehran', postal_code=1234567890,
                                               address_detail='somewhere', customer=self.customer1)
        self.address2 = Address.objects.create(state='Mashhad', city='Mashhad', postal_code=1234567891,
                                               address_detail='somewhere', customer=self.customer2)

        # Carts

        self.cart1 = Cart.objects.create(customer=self.customer1, off_code=self.off_code1, address=self.address1)
        self.cart2 = Cart.objects.create(customer=self.customer2, off_code=self.off_code2, address=self.address2)

        # cart items

        self.cart_item1 = CartItem.objects.create(cart=self.cart1, product=self.product1, count=2)
        self.cart_item2 = CartItem.objects.create(cart=self.cart1, product=self.product2, count=3)

        self.cart_item3 = CartItem.objects.create(cart=self.cart2, product=self.product3, count=4)
        self.cart_item4 = CartItem.objects.create(cart=self.cart2, product=self.product4, count=5)

    def test1_total_worth_success(self):
        total_price = self.cart1.total_worth()
        sum_item_prices = self.cart_item1.product.final_price + self.cart_item2.product.final_price

        self.assertGreater(total_price, 0)
        self.assertEqual(total_price, sum_item_prices)

    def test2_final_worth_success(self):
        total_price = self.cart1.total_worth()

        self.assertLess(self.cart1.final_worth(), total_price)
        self.assertEqual(self.cart1.final_worth(), total_price - self.off_code1.profit_value(total_price))

    def test_update_inventory_success(self):
        cart = self.cart1
        cart_detail = cart.items.all().values_list('product__inventory', 'count')
        product_inventory = list(cart.items.all().values_list('product__inventory', flat=True)).copy()
        cart.update_inventory()
        self.assertEqual(list(map(lambda t: sum(t), cart_detail)), product_inventory, msg='lists are not same')
        # print(cart_detail)
        # print(product_inventory)

    def test_get_profit_success(self):
        cart = self.cart2
        self.assertEqual(cart.get_profit(), cart.total_worth() - cart.final_worth())
        cart.off_code.delete()
        self.assertEqual(cart.get_profit(), 0)


class OffCodeTest(TestCase):
    def setUp(self) -> None:
        self.off_code1 = OffCode.objects.create(value=10000, type='PER', code='123465', valid_from=timezone.now(),
                                                valid_to=timezone.now() + timedelta(days=1))

    def test1_is_active_success(self):
        off_code = self.off_code1

        self.assertTrue(off_code.valid_from <= timezone.now() < off_code.valid_to)


class CartItemTest(TestCase):
    def setUp(self) -> None:
        # brands
        self.brand1 = Brand.objects.create(name='iphone', country='USA')
        self.brand2 = Brand.objects.create(name='samsung', country='Japan')

        # categories
        self.category1 = Category.objects.create(name='electronic')
        self.category2 = Category.objects.create(name='Phone', root=self.category1)

        # discounts
        self.discount1 = Discount.objects.create(value=5000, type='PRI')
        self.discount2 = Discount.objects.create(value=20, type='PER', max_price=100000)

        # products
        self.product1 = Product.objects.create(name='X', price=100000, description='some text', inventory=5,
                                               brand=self.brand1,
                                               category=self.category2, discount=self.discount1, slug='some-text')
        self.product2 = Product.objects.create(name='J5 Pro', price=200000, description='some text', inventory=10,
                                               brand=self.brand2,
                                               category=self.category2, slug='another-text')

        # Cart requirements
        self.customer1 = Customer.objects.create_user('test1', 'test1@email.com', 'test1', gender=1,
                                                      phone_number='09123456789')
        self.off_code1 = OffCode.objects.create(value=5000, type='PRI', code='123465', valid_from=timezone.now(),
                                                valid_to=timezone.now() + timedelta(days=3))
        self.cart1 = Cart.objects.create(customer=self.customer1, off_code=self.off_code1)

        # cart items

        self.cart_item1 = CartItem.objects.create(cart=self.cart1, product=self.product1)
        self.cart_item2 = CartItem.objects.create(cart=self.cart1, product=self.product2)
