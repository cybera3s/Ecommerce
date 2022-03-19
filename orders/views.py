import time

import returns as returns
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView
from django.utils.translation import gettext as _
from customers.forms import AddressRegisterForm
from customers.models import Address
from orders.models import Cart, OffCode


class CartCheckOutView(LoginRequiredMixin, TemplateView):
    template_name = 'orders/cart/cart.html'

    def setup(self, request, *args, **kwargs):
        self.real_cart = Cart.objects.get(customer=request.user.customer, is_active=True)
        super().setup(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Cart Checkout')
        context['real_cart'] = self.real_cart
        return context

    def get_object(self, model_instance, pk):
        """
        get a queryset of model instance using it's primary key or raise http 404 error
        :param model_instance: An instance of model classes
        :param pk: primary key of model
        :return: a http 404 error or model queryset
        """
        try:
            return model_instance.objects.get(pk=pk)
        except model_instance.DoesNotExist:
            raise Http404()

    def post(self, request):
        # print(request.POST)
        data = request.POST
        real_cart = self.real_cart

        # AJAX Post request for setting off code
        if data.get('action') == "set_offcode":
            code = data['offcode']
            offcode = get_object_or_404(OffCode, code=code)

            if offcode.active:
                self.real_cart.off_code = offcode
                self.real_cart.save()
                return JsonResponse({'total_price': self.real_cart.final_worth()})
            # invalid off code
            return JsonResponse({'msg': 'Invalid code!'})

