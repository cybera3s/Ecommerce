from django.urls import path, include
from .api_views import *
from .api_urls import router
from .views import CustomerRegisterView, CustomerLoginView, CustomerLogoutView

app_name = 'customers'

urlpatterns = [
    path('register/', CustomerRegisterView.as_view(), name='customer_register'),
    path('login/', CustomerLoginView.as_view(), name='customer_login'),
    path('logout/', CustomerLogoutView.as_view(), name='customer_logout'),
    path('api/', include(router.urls)),
]
