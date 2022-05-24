from django.urls import path, include
from .api_urls import router
# from .views import *

app_name = 'comments'

urlpatterns = [
    # comment api urls
    path('api/', include(router.urls)),

]
