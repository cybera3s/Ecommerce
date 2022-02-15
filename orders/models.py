from datetime import timedelta

from django.core.validators import MinValueValidator
from django.utils import timezone
from core.models import BaseModel, BaseDiscount
from django.db import models
from customers.models import Customer
from product.models import Product


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
    total_price = models.PositiveIntegerField(default=0, verbose_name='Total Price')
    final_price = models.PositiveIntegerField(default=0, verbose_name='Final Price')
    off_code = models.ForeignKey('OffCode', on_delete=models.CASCADE, related_name='carts', null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='carts')

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

    count = models.PositiveIntegerField(default=1)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, related_name='items')
    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.count} of {self.product}'


class OffCode(BaseDiscount):
    """
        A class to implement off codes
    """
    valid_from = models.DateTimeField(validators=[MinValueValidator(timezone.now(), 'must be greater than now')])
    valid_to = models.DateTimeField(
        validators=[MinValueValidator(timezone.now() + timedelta(minutes=1), 'must be greater than now')])
    code = models.CharField(max_length=50, verbose_name='off code')

    def __str__(self):
        return f"Off Code {self.value}"
