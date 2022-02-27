from rest_framework import routers

from .api_views import CustomerViewSet

router = routers.DefaultRouter()

router.register('customer', CustomerViewSet)
