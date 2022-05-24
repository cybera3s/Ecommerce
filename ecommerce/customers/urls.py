from django.urls import path, include
from .api_urls import router
from .views import *

app_name = 'customers'

urlpatterns = [
    path('register/', CustomerRegisterView.as_view(), name='customer_register'),
    path('login/', CustomerLoginView.as_view(), name='customer_login'),
    path('logout/', CustomerLogoutView.as_view(), name='customer_logout'),

    # Password Reset
    path('reset/', UserPasswordResetView.as_view(), name='reset_password'),
    path('reset/done/', UserPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('confirm/<uidb64>/<token>/', UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('confirm/complete', UserPasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # Dashboard URLs
    path('profile/', CustomerProfileView.as_view(), name='customer_profile'),
    path('dashboard/orders/', DashboardOrdersView.as_view(), name='dashboard_orders'),
    path('dashboard/addresses/', DashboardAddressView.as_view(), name='dashboard_addresses'),
    path('dashboard/user_info/', DashboardUserInfoView.as_view(), name='dashboard_user_info'),
    path('dashboard/user_info/change_password', ChangePasswordView.as_view(), name='change_password_user_info'),


    path('api/', include(router.urls)),
]
