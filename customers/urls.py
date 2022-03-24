from django.urls import path, include
from .api_views import *
from .api_urls import router
from .views import CustomerRegisterView, CustomerLoginView, CustomerLogoutView, CustomerProfileView, DashboardOrdersView

app_name = 'customers'

urlpatterns = [
    path('register/', CustomerRegisterView.as_view(), name='customer_register'),
    path('login/', CustomerLoginView.as_view(), name='customer_login'),
    # Dashboard URLs
    path('profile/', CustomerProfileView.as_view(), name='customer_profile'),
    path('dashboard/orders/', DashboardOrdersView.as_view(), name='dashboard_orders'),
    path('logout/', CustomerLogoutView.as_view(), name='customer_logout'),
    path('api/', include(router.urls)),
]
