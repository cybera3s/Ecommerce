from django.shortcuts import render
from django.views.generic import TemplateView


class CartCheckOutView(TemplateView):
    template_name = 'orders/cart/cart.html'
