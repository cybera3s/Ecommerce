from product.models import Product, Brand, Discount, Category
from django.test import TestCase


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
        # print(Product.highest_price())
        self.assertEqual(Product.highest_price(), self.product2)

    def test_calculate_inventory_success(self):
        product = self.product3
        self.assertEqual(product.inventory - 5, product.calculate_inventory(5))

    def test_get_absolute_url(self):
        # print(self.product1.get_absolute_url())
        self.assertEqual(self.product1.get_absolute_url(), f'/en/product/{self.product1.id}/{self.product1.slug}')
