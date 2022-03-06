from django.db import models
from core.models import BaseModel, User
from customers.models import Customer
from product.models import Product
from django.utils.translation import gettext_lazy as _


class Comment(BaseModel):
    can_publish = models.BooleanField(default=False, verbose_name=_('Can Publish'))
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='ucomments', verbose_name=_('User'))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='pcomments', verbose_name=_('Product'))
    reply = models.ForeignKey('self', on_delete=models.CASCADE, related_name='rcomments', blank=True, null=True, verbose_name=_('Reply'))
    is_reply = models.BooleanField(default=False, verbose_name=_('Is Reply?'))
    body = models.TextField(max_length=400, verbose_name=_('Body'))

    def __str__(self):
        return f'{self.user} - {self.body[:30]}'