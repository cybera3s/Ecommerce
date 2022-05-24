from rest_framework import routers

from .api_views import CustomerViewSet, AddressViewSet

router = routers.DefaultRouter()

router.register('customer', CustomerViewSet)
router.register('address', AddressViewSet)
