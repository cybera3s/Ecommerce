import json

from core.models import Setting
from product.models import Category
from utils.cart import Cart


def access_category_items(request):
    """
      The context processor to access categories in all pages
    """
    categories = Category.objects.all()
    return {'nav_categories': categories}


def cart(request):
    active_cart = Cart(request)

    if request.user.is_authenticated and hasattr(request.user, 'customer'):
        active_cart.merge_db_cart(request)
    # print('in context context processor : ', active_cart.cart)

    return {
        'cart': active_cart
    }


def app_settings(request):
    """Global values to pass to templates"""
    settings_dict = dict()
    settings = dict()
    for obj in Setting.objects.all():
        settings[obj.name] = obj.value
    settings_dict['settings'] = json.dumps(settings)
    return settings_dict
