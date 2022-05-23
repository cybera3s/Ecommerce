from django.db import models
from core.models import User
from django.utils.translation import gettext as _
from core.models import BaseModel
from utils.utils import user_avatar_path


class Customer(models.Model):
    """
        A class used to implement customers
    """
    user = models.OneToOneField(User, on_delete=models.RESTRICT, verbose_name=_('User'))
    gender = models.IntegerField(choices=[(1, 'male'), (2, 'female'), (3, 'other'), ], verbose_name=_('Gender'))
    avatar = models.FileField(upload_to=user_avatar_path, verbose_name=_('Avatar'), null=True,
                              blank=True, default='customers/images/default_avatar.jpg')

    def get_current_orders(self):
        """
        return active carts (open carts)
        """
        return self.carts.filter(is_active=True)

    def get_finished_orders(self):
        """
            return finished carts
        """
        return self.carts.filter(is_active=False)

    class Meta:
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')

    def __str__(self):
        return self.user.username


class Address(BaseModel):
    """
        A class used to implement customers
    """
    state = models.CharField(max_length=50, verbose_name=_('State'))
    city = models.CharField(max_length=50, verbose_name=_('City'))
    postal_code = models.IntegerField(verbose_name=_('Postal Code'), unique=True)
    address_detail = models.TextField(verbose_name=_('Address Detail'))
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='addresses',
                                 verbose_name=_('Customer'))

    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')

    def __str__(self):
        return f'{self.state} - {self.city} - {self.postal_code}'
