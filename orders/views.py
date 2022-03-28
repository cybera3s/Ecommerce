import time
from django.contrib import messages
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
        if request.user.is_authenticated:
            self.real_cart = Cart.objects.get(customer=request.user.customer, is_active=True)
        super().setup(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Cart Checkout')
        context['real_cart'] = self.real_cart
        return context

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
                data = {'total_price': self.real_cart.final_worth(), 'offcode': str(offcode), 'code': offcode.code,
                        'valid_to': offcode.valid_to}

                return JsonResponse(data)
            # invalid off code
            raise Http404()

        # AJAX Post request for setting address
        elif data.get('action') == "set_address":
            address = get_object_or_404(Address, pk=data['address'])
            real_cart.address = address
            real_cart.save()
            return JsonResponse({'msg': f'Address {address.id} was set!'})

        # AJAX POST request for add new address
        elif data.get('action') == 'new_address':
            form = AddressRegisterForm(request.POST)
            if form.is_valid():
                new_address = form.save(commit=False)
                new_address.customer = request.user.customer
                new_address.save()
                return JsonResponse({'address_id': new_address.id, 'address': str(new_address)})
            return JsonResponse({'msg': form.errors}, status=400)


class PaymentView(LoginRequiredMixin, View):
    def get(self, request):
        real_cart = Cart.objects.get(customer=request.user.customer, is_active=True)

        if hasattr(real_cart, 'address') and real_cart.items.all():
            real_cart.deactivate()
            real_cart.save()
            real_cart.update_inventory()
            time.sleep(5)
            return redirect('product:landing')
        return redirect('orders:cart_checkout')