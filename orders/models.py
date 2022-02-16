from datetime import timedelta
from django.core.validators import MinValueValidator, MinLengthValidator
from django.utils import timezone
from core.models import BaseModel, BaseDiscount
from django.db import models
from customers.models import Customer
from product.models import Product
from product.models import Category
from django.utils.translation import gettext as _


class Cart(BaseModel):
    """
        A class used to implement carts

        attributes:

            total_price: a positive integer\n
            final_price: a positive integer\n
            off_code: foreign key to OffCode Model\n
            customer: foreign key to customer Model\n

        methods:
            total_worth: calculate sum of items prices without considering off code\n
            final_worth: calculate  sum of items prices *By considering* off code
    """
    total_price = models.PositiveIntegerField(default=0, verbose_name=_('Total Price'))
    final_price = models.PositiveIntegerField(default=0, verbose_name=_('Final Price'))
    off_code = models.ForeignKey('OffCode', on_delete=models.CASCADE, related_name='carts', null=True, blank=True,
                                 verbose_name=_('Off Code'))
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name='carts', verbose_name=_('Customer'))

    class Meta:
        verbose_name = _('Cart')
        verbose_name_plural = _('Carts')

    def total_worth(self):
        """
            calculate total price of cart
        :return: total price amount (int)
        """
        self.total_price = sum([item.product.final_price for item in self.items.all()])
        return self.total_price

    def final_worth(self):
        """
        calculate final price of cart e.g with considering discounts
        :return: final price (int)
        """
        total = self.total_worth()
        self.final_price = total - self.off_code.profit_value(total) if self.off_code else total
        return self.final_price


class CartItem(BaseModel):
    """
        A class used to implement cart items
    """

    count = models.PositiveIntegerField(default=1, verbose_name=_('Count'))
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, related_name='items', verbose_name=_('Cart'))
    product = models.OneToOneField(Product, on_delete=models.CASCADE, verbose_name=_('Product'))

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    @classmethod
    def filter_by_category(cls, category: Category):
        """
        filter products by a Category
        :param category: (category object)
        :return: products with corresponding category
        """
        return cls.objects.filter(category=category)

    @classmethod
    def filter_by_product(cls, product: Product):
        """
         filter Cart Items by a specific product
        :param product: (product object)
        :return: cart items with corresponding product
        """
        return cls.objects.filter(product=product)

    @classmethod
    def filter_by_product_category(cls, category: Category):
        """
         filter Cart Items that their product consist of this category
        :param category: ( category object )
        :return: cart items with corresponding product category
        """
        return cls.objects.filter(product__category=category)

    def __str__(self):
        return f'{self.count} of {self.product}'


class OffCode(BaseDiscount):
    """
        A class to implement off codes
    """
    valid_from = models.DateTimeField(validators=[MinValueValidator(timezone.now(), _('must be greater than now'))],
                                      verbose_name=_('Valid From'))
    valid_to = models.DateTimeField(
        validators=[MinValueValidator(timezone.now() + timedelta(minutes=1), _('must be greater than now'))],
        verbose_name=_('Valid To'))
    code = models.CharField(max_length=50, verbose_name=_('Off Code'),
                            validators=[MinLengthValidator(5, _('must be more than five letters'))])

    @property
    def active(self):
        if self.valid_from < timezone.now() < self.valid_to:
            return True
        return False

    class Meta:
        verbose_name = _('Off Code')
        verbose_name_plural = _('Off Codes')

    def __str__(self):
        return f"Off Code {self.value}"
