from datetime import timedelta

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MinLengthValidator
from django.utils import timezone
from core.models import BaseModel, BaseDiscount
from django.db import models
from customers.models import Customer, Address
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
    total_price = models.PositiveIntegerField(default=0, verbose_name=_('Total Price'), null=True, blank=True)
    final_price = models.PositiveIntegerField(default=0, verbose_name=_('Final Price'), null=True, blank=True)
    off_code = models.OneToOneField('OffCode', on_delete=models.CASCADE, related_name='carts', null=True, blank=True,
                                    verbose_name=_('Off Code'))
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='carts', verbose_name=_('Customer'))
    address = models.ForeignKey(Address, on_delete=models.RESTRICT, related_name='carts', verbose_name=_('Address'),
                                null=True, blank=True)

    class Meta:
        verbose_name = _('Cart')
        verbose_name_plural = _('Carts')

    def total_worth(self):
        """
            calculate total price of cart
        :return: total price amount (int)
        """
        self.total_price = sum([item.product.final_price * item.count for item in self.items.all()])
        return self.total_price

    def final_worth(self):
        """
        calculate final price of cart e.g with considering discounts
        :return: final price (int)
        """
        total = self.total_worth()
        self.final_price = total - self.off_code.profit_value(total) if self.off_code else total
        return self.final_price

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        """
        save calculated prices in db
        """
        self.total_price = self.total_worth()
        self.final_price = self.final_worth()
        super().save(force_insert, force_update, using, update_fields)

    def update_inventory(self):
        """update products inventory of cart items """
        if self.items.all():
            for item in self.items.all():
                item.product.calculate_inventory(item.count)

    def get_profit(self):
        """
        calculate profit of cart
        """
        return self.total_worth() - self.final_worth() if self.off_code else 0


class CartItem(BaseModel):
    """
        A class used to implement cart items
    """

    count = models.PositiveIntegerField(default=1, verbose_name=_('Count'),
                                        validators=[MinValueValidator(1, message='minimum count is 1')])
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, related_name='items', verbose_name=_('Cart'))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('Product'))

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def clean(self):
        """
        check and validate count to not be greater than product inventory
        :return:
        """
        if self.count > self.product.inventory:
            raise ValidationError('Maximum count is exceeded')

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
        show = f"%{self.value}" if self.type == 'PER' else f"${self.value}"
        return show
