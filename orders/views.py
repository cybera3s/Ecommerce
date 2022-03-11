from django.shortcuts import render
from django.views.generic import TemplateView
from core.utils.cart import Cart
from django.utils.translation import gettext as _


class CartCheckOutView(TemplateView):
    template_name = 'orders/cart/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('landing')
        context['cart'] = Cart(self.request)

        return context
