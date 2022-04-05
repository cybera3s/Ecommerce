from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from core.models import User
from utils.cart import Cart
from .forms import CustomerRegistrationForm, CustomerLoginForm, CustomerEditProfileForm, CustomerChangePassword
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
                cart.register_in_db(request)  # Register items in cookie in db
                response = remove_cookie(redirect('customers:customer_profile'), 'cart')  # del cart cookie

                # messages.success(request, _('logged in successfully'), 'success')
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


class CustomerProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'customers/dashboard/dashboard.html'


class DashboardOrdersView(LoginRequiredMixin, TemplateView):
    template_name = 'customers/dashboard/orders/orders.html'


class DashboardAddressView(LoginRequiredMixin, TemplateView):
    template_name = 'customers/dashboard/addresses/addresses.html'


class DashboardUserInfoView(LoginRequiredMixin, TemplateView):
    template_name = 'customers/dashboard/user_info/user_info.html'
    form_class = CustomerEditProfileForm
    form_class1 = CustomerChangePassword

    def get_context_data(self):
        context = super().get_context_data()
        context['form'] = self.form_class(self.request.user.customer,
                                          initial={'email': self.request.user.email,
                                                   'first_name': self.request.user.first_name,
                                                   'last_name': self.request.user.last_name,
                                                   'phone_number': self.request.user.phone,
                                                   'gender': self.request.user.customer.gender})
        context['cp_form'] = self.form_class1()
        return context

    def post(self, request):
        form = self.form_class(request.user.customer, request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            customer = request.user.customer
            customer.gender = cd['gender']
            customer.avatar = request.FILES.get('avatar')
            user = request.user
            user.email = cd['email']
            user.first_name = cd['first_name']
            user.last_name = cd['last_name']
            user.phone = cd['phone_number']
            user.save()
            customer.save()
            messages.success(request, _('Personal Information Updated!'), 'success personal_info')
            return redirect('customers:dashboard_user_info')
        # Handle Invalid Form
        messages.error(request, _('Please correct Below Errors!'), 'error')
        return render(request, self.template_name, {'form': form, 'cp_form': self.form_class1()})


class ChangePasswordView(LoginRequiredMixin, View):
    form_class = CustomerChangePassword
    form_class1 = CustomerEditProfileForm

    template_name = 'customers/dashboard/user_info/user_info.html'

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            request.user.set_password(cd['password'])
            request.user.save()
            messages.success(request, _('Password successfully Updated!'), 'success change_password')
            return redirect('customers:dashboard_user_info')
        # Handle Invalid Form
        messages.error(request, _('Please correct Below Errors!'), 'error change_password')
        initial = {'email': request.user.email,
                   'first_name': request.user.first_name,
                   'last_name': request.user.last_name,
                   'phone_number': request.user.phone,
                   'gender': request.user.customer.gender}
        return render(request, self.template_name,
                      {'cp_form': form, 'form': self.form_class1(request.user.customer, initial=initial)})
