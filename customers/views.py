from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from core.models import User
from utils.cart import Cart
from .forms import CustomerRegistrationForm, CustomerLoginForm
from .models import Customer
from django.utils.translation import gettext as _
from utils.client import remove_cookie


class CustomerRegisterView(View):
    """register customer view"""
    template_name = 'customers/register.html'
    form_class = CustomerRegistrationForm
    data = {
        'title': 'Register',
        'form': form_class
    }

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('product:landing')
        else:
            return super().dispatch(request, *args, **kwargs)

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

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('product:landing')
        else:
            return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, self.data)

    def setup(self, request, *args, **kwargs):
        self.next = request.GET.get('next')
        return super().setup(request, *args, **kwargs)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, phone=cd['phone'], password=cd['password'])
            if user is not None:
                login(request, user)

                cart = Cart(request)
                cart.register_in_db(request)            # Register items in cookie in db
                response = remove_cookie(redirect('product:landing'), 'cart')          # del cart cookie

                messages.success(request, _('logged in successfully'), 'success')
                if self.next:
                    return remove_cookie(redirect(self.next), 'cart')

                return response
            # Handle invalid username or password
            messages.error(request, _('Username or Password is Incorrect'), 'warning')

        # Handle Invalid form
        self.data['form'] = form
        return render(request, self.template_name, self.data)


class CustomerLogoutView(LoginRequiredMixin, View):
    """user logout view"""

    def get(self, request):
        logout(request)
        # del cart cookie on logout
        response = remove_cookie(redirect('product:landing'), 'cart')
        return response
