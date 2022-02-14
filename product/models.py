from django.db import models
from core.models import BaseModel


class Product(BaseModel):
    """
        A class used to implement products
    """
    name = models.CharField(max_length=100, verbose_name='Name')
    price = models.PositiveIntegerField(default=0, verbose_name='Price')
    description = models.TextField()
    picture = models.FileField(verbose_name='product image', null=True, blank=True)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    discount = models.ForeignKey('Discount', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'