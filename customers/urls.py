from django.urls import path
from .views import CustomerRegisterView, CustomerLoginView
app_name = 'customers'

urlpatterns = [
    path('register/', CustomerRegisterView.as_view(), name='customer_register'),
    path('login/', CustomerLoginView.as_view(), name='customer_login'),
]
