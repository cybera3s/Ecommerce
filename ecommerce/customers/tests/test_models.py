from customers.models import Customer, Address
from orders.models import OffCode, Cart, CartItem
from product.models import Product, Brand, Discount, Category
from django.test import TestCase
from datetime import timedelta
from django.utils import timezone
from core.models import User


class CustomerTest(TestCase):
    def setUp(self) -> None:
        # customers
        self.user1 = User.objects.create_user(email='test1@email.com', phone='09224023292', password='1234')
        self.customer1 = Customer.objects.create(gender=1, user=self.user1)
        # brands
        self.brand1 = Brand.objects.create(name='HP', country='Japan')
        self.brand2 = Brand.objects.create(name='Samsung', country='Korea')

        # categories
        self.category1 = Category.objects.create(name='Digital')
        self.category2 = Category.objects.create(name='Mobile', root=self.category1)

        # discounts
        self.discount1 = Discount.objects.create(value=1000, type='PRI')
        self.discount2 = Discount.objects.create(value=20, type='PER')

        # products
        self.product1 = Product.objects.create(name='TV', price=100000, description='test', inventory=5,
                                               brand=self.brand1,
                                               category=self.category1, discount=self.discount1, slug='some-text')
        self.product2 = Product.objects.create(name='J5', price=200000, description='test2', inventory=10,
                                               brand=self.brand2,
                                               category=self.category2, slug='another-text')

        # Cart requirements

        self.off_code1 = OffCode.objects.create(value=10000, type='PRI', code='123465', valid_from=timezone.now(),
                                                valid_to=timezone.now() + timedelta(days=5))
        self.cart1 = Cart.objects.create(customer=self.customer1, off_code=self.off_code1)
        self.cart2 = Cart.objects.create(customer=self.customer1)

        # cart items

        self.cart_item1 = CartItem.objects.create(cart=self.cart1, product=self.product1)
        self.cart_item2 = CartItem.objects.create(cart=self.cart1, product=self.product2)

    def test1_customer_create_success(self):
        # print(self.user1)
        # print(self.customer1)
        self.assertIsInstance(self.customer1, Customer)
        self.assertEqual(self.user1.username, self.customer1.__str__())

    def test2_get_current_orders_success(self):
        # print(self.customer1.carts.filter(is_active=True))
        self.assertIn(self.cart1, self.customer1.get_current_orders())
        self.assertTrue(all(map(lambda cart: cart.is_active, self.customer1.get_current_orders())))

    def test3_get_finished_orders(self):
        self.cart1.deactivate()
        self.assertEqual(self.customer1.get_finished_orders().first().is_active, False)
        self.assertNotIn(self.cart2, self.customer1.get_finished_orders())


class AddressTest(TestCase):
    def setUp(self) -> None:
        # customers
        self.user1 = User.objects.create_user(email='test1@email.com', phone='09224023292', password='1234')
        self.customer1 = Customer.objects.create(gender=1, user=self.user1)

        # addresses
        self.address1 = Address.objects.create(state='Tehran', city='Karaj', postal_code=1234567890,
                                               address_detail='somewhere', customer=self.customer1)

    def test1_address_create_success(self):
        # print(self.address1.__str__())
        self.assertIsInstance(self.address1, Address)

