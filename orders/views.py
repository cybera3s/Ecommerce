import time
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.views import View
from django.views.generic import TemplateView
from django.utils.translation import gettext as _
from customers.forms import AddressRegisterForm
from customers.models import Address
from orders.models import Cart, OffCode


class CartCheckOutView(LoginRequiredMixin, TemplateView):
    template_name = 'orders/cart/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Cart Checkout')
        context['real_cart'] = Cart.objects.get(customer=self.request.user.customer, is_active=True)
        return context
