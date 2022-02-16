from django.db import models
from django.db.models import Max
from core.models import BaseModel, BaseDiscount
from django.utils.translation import gettext as _


class Product(BaseModel):
    """
        A class used to implement products
    """
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    price = models.PositiveIntegerField(default=0, verbose_name=_('Price'))
    description = models.TextField(verbose_name=_('Description'))
    picture = models.FileField(verbose_name=_('Product Image'), null=True, blank=True)
    inventory = models.PositiveIntegerField(verbose_name=_('Inventory'))
    slug = models.SlugField(max_length=30, help_text=_('A short label for product'), verbose_name=_('Slug'))
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE, verbose_name=_('Brand'))
    discount = models.ForeignKey('Discount', on_delete=models.CASCADE, blank=True, null=True,
                                 verbose_name=_('Discount'))
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name=_('Category'))

    class Meta:
        ordering = ['-created']
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    @property
    def is_available(self):
        return self.inventory > 0

    @property
    def final_price(self):
        """
        calculate price with discounts
        :return:
        """
        return self.price - self.discount.profit_value(self.price) if self.discount else self.price

    @classmethod
    def highest_price(cls):
        """
        Returns the product with the highest price
        """
        highest = cls.objects.aggregate(max_price=Max('price'))['max_price']
        return cls.objects.get(price=highest)

    def __str__(self):
        return f'{self.name}'


class Brand(BaseModel):
    """
        implement brands
    """
    name = models.CharField(max_length=50, verbose_name='Name')
    country = models.CharField(max_length=50, verbose_name='Country')

    def __str__(self):
        return self.name


class Category(BaseModel):
    """
        implement categories
    """
    name = models.CharField(max_length=100, verbose_name='Name')
    root = models.ForeignKey('self', on_delete=models.CASCADE, default=None, null=True, blank=True)
    discount = models.ForeignKey('Discount', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Discount(BaseDiscount):
    """
        Implement discounts
    """

    def __str__(self):
        return f'Discount {self.value}'
