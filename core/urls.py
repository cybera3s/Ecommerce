from django.urls import path
from django.views.generic import TemplateView

app_name = 'core'

urlpatterns = [
    path('about/', TemplateView.as_view(template_name='core/about.html'), name='about'),
    path('connect_us/', TemplateView.as_view(template_name='core/contact_us.html'), name='contact_us'),

]
