from rest_framework import routers
from .api_views import *

router = routers.DefaultRouter()

router.register('comments', CommentViewSet)