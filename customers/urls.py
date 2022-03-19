from django.urls import path, include
from .api_views import *
from .api_urls import router
from .views import CustomerRegisterView, CustomerLoginView, CustomerLogoutView, CustomerProfileView

app_name = 'customers'

urlpatterns = [
    path('register/', CustomerRegisterView.as_view(), name='customer_register'),
    path('login/', CustomerLoginView.as_view(), name='customer_login'),
    path('profile/', CustomerProfileView.as_view(), name='customer_profile'),
    path('logout/', CustomerLogoutView.as_view(), name='customer_logout'),
    path('api/', include(router.urls)),
]
