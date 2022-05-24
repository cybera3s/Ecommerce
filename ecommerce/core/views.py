from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.utils.translation import gettext as _

from core.forms import ContactForm


class ContactUsView(TemplateView):
    template_name = 'core/contact_us.html'
    form_class = ContactForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            subject = "Contact Form Feedback"
            body = {
                'email': form.cleaned_data['email'],
                'message': form.cleaned_data['message'],
            }
            message = "From: " + body['email'] + "\nmessage: " + body['message']

            try:
                send_mail(subject, message, 'cybera.3s@gmail.com', ['cybera.3s@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, _('Thanks for your Feedback'), 'success contact_us')
            return redirect("core:contact_us")
        # handle Invalid form data
        messages.error(request, _('Please Correct Below errors'), 'error contact_us')
        return render(request, self.template_name, {'form': form})
