from orders.models import Cart, CartItem, OffCode
from customers.models import Customer
from product.models import Product, Brand, Discount, Category
from django.test import TestCase
from datetime import timedelta
from django.utils import timezone
from orders.serializers import CartItemSerializer
from core.models import User


class CartItemSerializerTest(TestCase):
    def setUp(self) -> None:
        #  customers
        self.user1 = User.objects.create_user(phone='09123456789', email='test@email.com', password='1234')
        self.customer1 = Customer.objects.create(user=self.user1, gender='1')

        # Products
        self.category1 = Category.objects.create(name='Electrical')
        self.brand1 = Brand.objects.create(name='all', country='Japan')

        self.product1 = Product.objects.create(name='a51', price=40000, description='some text',
                                               inventory=5,
                                               brand=self.brand1,
                                               category=self.category1, slug='some-text')
        self.product2 = Product.objects.create(name='s21 ultra', price=20000, description='some text',
                                               inventory=5, brand=self.brand1, category=self.category1, slug='text')
        # Orders
        self.cart1 = Cart.objects.create(customer=self.customer1)
        self.cartitem1 = CartItem.objects.create(product=self.product1, cart=self.cart1, count=5)
        self.cartitem3 = CartItem.objects.create(product=self.product2, cart=self.cart1, count=2)

        self.data1 = {'count': 2, 'cart': self.cart1.id, 'product': self.product1.id}

        self.ser1 = CartItemSerializer

    def test_save(self):
        ser = self.ser1(data=self.data1)
        if ser.is_valid():
            data = ser.validated_data
            ser.save()

