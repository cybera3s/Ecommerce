from django.urls import path
from .views import *

app_name = 'product'

urlpatterns = [
    path('', LandingView.as_view(), name='landing'),
]
