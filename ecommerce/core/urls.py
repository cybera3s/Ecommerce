from django.urls import path
from django.views.generic import TemplateView
from .views import ContactUsView
app_name = 'core'

urlpatterns = [
    path('about/', TemplateView.as_view(template_name='core/about.html'), name='about'),
    path('connect_us/', ContactUsView.as_view(), name='contact_us'),

]
