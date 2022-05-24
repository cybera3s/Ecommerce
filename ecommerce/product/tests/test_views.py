from django.test import TestCase
from django.urls import reverse

from product.models import Product, Category, Discount, Brand


class TestLandingView(TestCase):

    def setUp(self) -> None:
        self.brand1 = Brand.objects.create(name='LG', country='Japan')
        self.discount1 = Discount.objects.create(value=2000, type='PRI')
        self.category1 = Category.objects.create(name='Electrical')
        self.product1 = Product.objects.create(name='Power Bank', price=100000, description='some text', inventory=5,
                                               brand=self.brand1,
                                               category=self.category1, discount=self.discount1, slug='some-text')

    def test_get_method(self):
        response = self.client.get(reverse('product:landing'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['products'].first(), Product)
        self.assertEqual(len(response.context['products']), 1)
        self.assertEqual(response.context['title'], 'landing')
        self.assertQuerysetEqual(response.context['brands'], Brand.objects.all())


class TestCategoryListView(TestCase):

    def setUp(self) -> None:
        self.category1 = Category.objects.create(name='Electrical')
        self.category2 = Category.objects.create(name='mobile', root=self.category1)
        self.category3 = Category.objects.create(name='Laptop', root=self.category1)

    def test_get_method(self):
        response = self.client.get(reverse('product:category_list'))
        self.assertEqual(response.status_code, 200)
        #
        self.assertIsInstance(response.context['categories'].first(), Category)
        self.assertEqual(len(response.context['categories']), 1)
