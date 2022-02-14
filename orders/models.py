from core.models import BaseModel
from django.db import models


class CartItem(BaseModel):
    """
        A class used to implement cart items
    """

    count = models.PositiveIntegerField(default=1)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    product = models.OneToOneField('Product', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.count} of {self.product}'