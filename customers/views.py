from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from core.models import User
from .forms import CustomerRegistrationForm, CustomerLoginForm
from .models import Customer
from django.utils.translation import gettext as _


class CustomerRegisterView(View):
    """register customer view"""
    template_name = 'customers/register.html'
    form_class = CustomerRegistrationForm
    data = {
        'title': 'Register',
        'form': form_class
    }

    def get(self, request):
        return render(request, self.template_name, self.data)

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            new_user = User.objects.create_user(phone=cd['phone'], email=cd['email'], password=cd['password'])
            Customer.objects.create(user=new_user, gender=cd['gender'])
            messages.success(request, 'Registered successfully !', 'success')
            return redirect('customers:customer_login')

        # Handle Invalid form
        self.data['form'] = form
        return render(request, self.template_name, self.data)


class CustomerLoginView(View):
    template_name = 'customers/login.html'
    form_class = CustomerLoginForm
    data = {
        'title': _('Login'),
        'form': form_class
    }

    def get(self, request):
        return render(request, self.template_name, self.data)