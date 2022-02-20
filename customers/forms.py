from django import forms


# from django.core.exceptions import ValidationError
# from .models import Customer


class CustomerRegistrationForm(forms.Form):
    GENDER_CHOICES = [('0', 'select your gender'), ('1', 'Male'), ('2', 'Female'), ('3', 'Other')]

    phone = forms.CharField(max_length=100,
                            widget=forms.TextInput(
                                attrs={'class': 'form-control', 'type': 'tel', 'placeholder': 'phone'}))
    email = forms.EmailField(max_length=100,
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES,
                               widget=forms.Select(attrs={'class': 'form-select mb-3', 'placeholder': 'Gender'}))

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    confirm_password = forms.CharField(label='confirm password',
                                       widget=forms.PasswordInput(
                                           attrs={'class': 'form-control', 'placeholder': 'confirm password'}))
