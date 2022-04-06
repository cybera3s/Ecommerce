from django.core.exceptions import ValidationError
from core.models import User
from orders.models import Cart, CartItem, OffCode
from customers.models import Customer, Address
from product.models import Product, Brand, Discount, Category
from django.test import TestCase
from datetime import timedelta
from django.utils import timezone


class ProductTest(TestCase):
    def setUp(self) -> None:
        # brands
        self.brand1 = Brand.objects.create(name='LG', country='Japan')
        self.brand2 = Brand.objects.create(name='samsung', country='Korea')
        self.brand3 = Brand.objects.create(name='Lenovo', country='China')

        # discounts
        self.discount1 = Discount.objects.create(value=2000, type='PRI')
        self.discount2 = Discount.objects.create(value=15, type='PER')
        self.discount3 = Discount.objects.create(value=10, type='PER')

        # categories
        self.category1 = Category.objects.create(name='Electrical')
        self.category2 = Category.objects.create(name='mobile', root=self.category1, discount=self.discount3)
        self.category3 = Category.objects.create(name='Laptop', root=self.category1)

        # products
        self.product1 = Product.objects.create(name='Power Bank', price=100000, description='some text', inventory=5,
                                               brand=self.brand1,
                                               category=self.category1, discount=self.discount1, slug='some-text')
        self.product2 = Product.objects.create(name='J7', price=200000, description='some text', inventory=10,
                                               brand=self.brand2,
                                               category=self.category2, slug='another-text', discount=self.discount2)

        self.product3 = Product.objects.create(name='a52', price=10000, description='a51', inventory=5,
                                               brand=self.brand2,
                                               category=self.category2, slug='another-text')
        self.product4 = Product.objects.create(name='Z-book1', price=10000, description='Z-book1', inventory=5,
                                               brand=self.brand3,
                                               category=self.category3, slug='another-text')

    def test_create_success(self):
        self.assertIsInstance(self.product1, Product)
        self.assertTrue(str(self.product1))

    def test_is_available_success(self):
        self.assertTrue(self.product1.is_available)
        self.assertGreater(self.product1.inventory, 0)

    def test_final_price_success(self):
        product = self.product2
        sum_discount = product.discount.profit_value(product.price) + product.category.discount.profit_value(
            product.price)
        self.assertEqual(product.final_price, product.price - sum_discount)
        self.assertEqual(self.product1.final_price, self.product1.price - 2000)
        self.assertTrue(product.final_price)

    def test_highest_price_success(self):
        print(Product.highest_price())
        self.assertEqual(Product.highest_price(), self.product2)

    def test_calculate_inventory_success(self):
        product = self.product3
        self.assertEqual(product.inventory - 5, product.calculate_inventory(5))

    def test_get_absolute_url(self):
        print(self.product1.get_absolute_url())
        self.assertEqual(self.product1.get_absolute_url(), f'/en/product/{self.product1.id}/{self.product1.slug}')

# class OffCodeTest(TestCase):
#     def setUp(self) -> None:
#         self.off_code1 = OffCode.objects.create(value=10000, type='PER', code='123465', valid_from=timezone.now(),
#                                                 valid_to=timezone.now() + timedelta(days=1))
#
#     def test1_is_active_success(self):
#         off_code = self.off_code1
#
#         self.assertTrue(off_code.active)
#
#     def test_is_active_fail(self):
#         off_code = self.off_code1
#         off_code.valid_from = timezone.now() - timedelta(days=2)
#         off_code.valid_to = timezone.now() - timedelta(days=1)
#         self.assertFalse(off_code.active)
#
#
# class CartItemTest(TestCase):
#     def setUp(self) -> None:
#         # brands
#         self.brand1 = Brand.objects.create(name='LG', country='Japan')
#         self.brand2 = Brand.objects.create(name='samsung', country='Korea')
#         self.brand3 = Brand.objects.create(name='Lenovo', country='China')
#
#         # categories
#         self.category1 = Category.objects.create(name='Electrical')
#         self.category2 = Category.objects.create(name='mobile', root=self.category1)
#         self.category3 = Category.objects.create(name='Laptop', root=self.category1)
#
#         # discounts
#         self.discount1 = Discount.objects.create(value=2000, type='PRI')
#         self.discount2 = Discount.objects.create(value=35, type='PER')
#
#         self.off_code1 = OffCode.objects.create(value=10000, type='PRI', code='123465', valid_from=timezone.now(),
#                                                 valid_to=timezone.now() + timedelta(days=5))
#         self.off_code2 = OffCode.objects.create(value=20, type='PER', code='abed', valid_from=timezone.now(),
#                                                 valid_to=timezone.now() + timedelta(days=2))
#         # products
#         self.product1 = Product.objects.create(name='TV', price=100000, description='some text', inventory=5,
#                                                brand=self.brand1,
#                                                category=self.category1, discount=self.discount1, slug='some-text')
#         self.product2 = Product.objects.create(name='J5', price=200000, description='some text', inventory=10,
#                                                brand=self.brand2,
#                                                category=self.category2, slug='another-text')
#
#         self.product3 = Product.objects.create(name='a51', price=10000, description='a51', inventory=5,
#                                                brand=self.brand2,
#                                                category=self.category2, slug='another-text')
#         self.product4 = Product.objects.create(name='Z-book', price=10000, description='Z-book', inventory=5,
#                                                brand=self.brand3,
#                                                category=self.category3, slug='another-text')
#         # customers
#         self.user1 = User.objects.create_user(email='test1@email.com', phone='09224023292', password='1234')
#         self.customer1 = Customer.objects.create(gender=1, user=self.user1)
#
#         self.user2 = User.objects.create_user(email='test2@email.com', phone='09123456789', password='1234')
#         self.customer2 = Customer.objects.create(gender=1, user=self.user2)
#         # addresses        print(self.cart_item1.filter_by_product(self.product1))
#
#         self.address1 = Address.objects.create(state='Tehran', city='Tehran', postal_code=1234567890,
#                                                address_detail='somewhere', customer=self.customer1)
#         self.address2 = Address.objects.create(state='Mashhad', city='Mashhad', postal_code=1234567891,
#                                                address_detail='somewhere', customer=self.customer2)
#
#         # Carts
#
#         self.cart1 = Cart.objects.create(customer=self.customer1, off_code=self.off_code1, address=self.address1)
#         self.cart2 = Cart.objects.create(customer=self.customer2, off_code=self.off_code2, address=self.address2)
#
#         # cart items
#
#         self.cart_item1 = CartItem.objects.create(cart=self.cart1, product=self.product1, count=2)
#         self.cart_item2 = CartItem.objects.create(cart=self.cart1, product=self.product2, count=3)
#
#         self.cart_item3 = CartItem.objects.create(cart=self.cart2, product=self.product3, count=4)
#         self.cart_item4 = CartItem.objects.create(cart=self.cart2, product=self.product4, count=5)
#
#     def test_create_success(self):
#         self.assertIsInstance(self.cart_item1, CartItem)
#         self.assertTrue(str(self.cart_item1))
#
#     def test_clean(self):
#         p = self.product4
#         item = self.cart_item4
#         item.count = 6
#         self.assertRaises(ValidationError, item.clean)
