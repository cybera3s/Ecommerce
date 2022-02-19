from django import forms


# from django.core.exceptions import ValidationError
# from .models import Customer


class CustomerRegistrationForm(forms.ModelForm):
    GENDER_CHOICES = [('1', 'Male'), ('2', 'Female'), ('3', 'Other')]

    phone = forms.CharField(max_length=100,
                            widget=forms.TextInput(attrs={'placeholder': 'your username', 'class': 'form-control'}))
    email = forms.EmailField(max_length=100,
                             widget=forms.EmailInput(attrs={'placeholder': 'your email', 'class': 'form-control'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'your password', 'class': 'form-control'}))
    confirm_password = forms.CharField(label='confirm password',
                                       widget=forms.PasswordInput(
                                           attrs={'placeholder': 'password confirmation', 'class': 'form-control'}))
