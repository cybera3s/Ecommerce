from django.apps import AppConfig
from django.utils.translation import gettext as _


class CustomersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customers'
    verbose_name = _('Customers')
