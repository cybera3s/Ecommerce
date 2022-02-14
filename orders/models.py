from core.models import BaseModel, BaseDiscount
from django.db import models
from customers.models import Customer


class Cart(BaseModel):
    """
        A class used to implement carts
    """
    total_price = models.PositiveIntegerField(default=0, verbose_name='Total Price')
    final_price = models.PositiveIntegerField(default=0, verbose_name='Final Price')
    off_code = models.ForeignKey('OffCode', on_delete=models.CASCADE, related_name='carts')
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, related_name='carts')

    def total_worth(self):
        """
            calculate total price of cart
        :return: total price amount (int)
        """
        self.total_price = sum([item.product.price for item in self.items.all()])
        return self.total_price


class CartItem(BaseModel):
    """
        A class used to implement cart items
    """

    count = models.PositiveIntegerField(default=1)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, related_name='items')
    product = models.OneToOneField('Product', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.count} of {self.product}'


class OffCode(BaseDiscount):
    """
        A class to implement off codes
    """
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    code = models.CharField(max_length=50, verbose_name='off code')

    def __str__(self):
        return f"Off Code {self.value}"