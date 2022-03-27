from django import forms
from django.core.exceptions import ValidationError
from core.models import User
from django.utils.translation import gettext as _
from customers.models import Address, Customer


class CustomerRegistrationForm(forms.Form):
    GENDER_CHOICES = [('0', _('select your gender')), ('1', _('Male')), ('2', _('Female')), ('3', _('Other'))]

    phone = forms.CharField(max_length=13,
                            widget=forms.TextInput(
                                attrs={'class': 'form-control', 'type': 'tel', 'placeholder': _('phone')}))
    email = forms.EmailField(max_length=100,
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': _('Email')}),
                           )
    gender = forms.ChoiceField(choices=GENDER_CHOICES,
                               widget=forms.Select(attrs={'class': 'form-select mb-3', 'placeholder': 'Gender'}))

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    confirm_password = forms.CharField(label=_('confirm password'),
                                       widget=forms.PasswordInput(
                                           attrs={'class': 'form-control', 'placeholder': _('confirm password')}))

    def clean_phone(self):
        """
        stop repetitious phone number
        """
        phone = self.cleaned_data['phone']
        user = User.objects.filter(username=phone).exists()
        if user:
            raise ValidationError(_('User with this phone number already exists!'))
        return phone

    def clean_email(self):
        """
        stop repetitious email
        """
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError('Email already exists!')
        return email

    def clean(self):
        """
        Check that passwords are the same
        """
        cd = super().clean()
        p1 = cd.get('password')
        p2 = cd.get('confirm_password')

        if p1 and p2 and p1 != p2:
            raise ValidationError(_('passwords does not match!'))


class CustomerLoginForm(forms.Form):
    phone = forms.CharField(max_length=100, label='Phone Number',
                            widget=forms.TextInput(
                                attrs={'placeholder': _('phone number or email'), 'class': 'form-control'}))
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(
                                   attrs={'placeholder': _('your password'), 'class': 'form-control'}))


class AddressRegisterForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ("state", 'city', 'postal_code', 'address_detail',)
        exclude = ('customer',)


class CustomerEditProfileForm(forms.Form):
    GENDER_CHOICES = [('0', _('select your gender')), ('1', _('Male')), ('2', _('Female')), ('3', _('Other'))]

    first_name = forms.CharField(label=_('First Name'), max_length=150, required=False)
    last_name = forms.CharField(label=_('Last Name'), max_length=150, required=False)
    email = forms.EmailField(label=_('Email'))
    phone_number = forms.CharField(label=_('Phone Number'), max_length=13, widget=forms.TextInput(
        attrs={'type': 'tel', 'placeholder': _('Phone Number')}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES,
                               widget=forms.Select(attrs={'placeholder': 'Gender', 'class': 'form-control'}))

    def __init__(self, customer, *args, **kwargs):
        self.customer = Customer.objects.get(id=customer.id)
        super(CustomerEditProfileForm, self).__init__(*args, **kwargs)

    def clean_email(self):
        """
        stop repetitious email
        """
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email)
        if self.customer.user != user.first():
            if user.exists():
                raise ValidationError('Email already exists!')
        return email

    def clean_phone_number(self):
        """
        stop repetitious email
        """
        phone_number = self.cleaned_data['phone_number']
        user = User.objects.filter(phone=phone_number)

        if self.customer.user != user.first():
            if user.exists():
                raise ValidationError(_('Phone Number already exists!'))
        return phone_number


class CustomerChangePassword(forms.Form):
    password = forms.CharField(label=_('Password'), widget=forms.PasswordInput(attrs={'placeholder': _('Password')}))
    confirm_password = forms.CharField(label=_('Confirm Password'),
                                       widget=forms.PasswordInput(attrs={'placeholder': _('Confirm password')}))

    def clean(self):
        """
        Check that passwords are the same
        """
        cd = super().clean()
        p1 = cd.get('password')
        p2 = cd.get('confirm_password')

        if p1 and p2 and p1 != p2:
            raise ValidationError(_('Passwords does not match!'))