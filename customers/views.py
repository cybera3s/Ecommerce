from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from .forms import CustomerRegistrationForm


class CustomerRegisterView(View):
    """register customer view"""
    template_name = 'customers/register.html'
    form_class = CustomerRegistrationForm
    data = {
        'title': 'Register',
    }

    def get(self, request):

        self.data['form'] = self.form_class
        return render(request, self.template_name, self.data)

