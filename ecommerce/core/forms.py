from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField(max_length=150)
    message = forms.CharField(widget=forms.Textarea, max_length=2000)
