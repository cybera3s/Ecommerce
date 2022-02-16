from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from core.models import BaseModel


class Customer(User):
    """
        A class used to implement customers
    """
    # first_name = models.CharField(max_length=32, verbose_name='First Name')
    # last_name = models.CharField(max_length=32, verbose_name='Last Name')
    # email = models.EmailField(verbose_name='Email')
    phone_number = models.CharField(max_length=32, verbose_name=_('Phone Number'))
    gender = models.IntegerField(choices=[(1, 'male'), (2, 'female'), (3, 'other'), ], verbose_name=_('Gender'))

    class Meta:
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')


class Address(BaseModel):
    """
        A class used to implement customers
    """
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    postal_code = models.IntegerField(verbose_name='Postal Code')
    address_detail = models.TextField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='addresses')

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return f'{self.state} - {self.city}'
