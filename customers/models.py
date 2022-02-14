from django.db import models
from django.contrib.auth.models import User
from core.models import BaseModel


class Customer(User):
    """
        A class used to implement customers
    """
    # first_name = models.CharField(max_length=32, verbose_name='First Name')
    # last_name = models.CharField(max_length=32, verbose_name='Last Name')
    # email = models.EmailField(verbose_name='Email')
    phone_number = models.CharField(max_length=32, verbose_name='Phone Number')
    gender = models.IntegerField(choices=[(1, 'male'), (2, 'female'), (3, 'other'), ])

