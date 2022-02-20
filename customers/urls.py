from django.urls import path
from .views import CustomerRegisterView
app_name = 'customers'

urlpatterns = [
    path('register/', CustomerRegisterView.as_view(), name='customer_register')
]
