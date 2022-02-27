from django.urls import path, include
from .api_urls import router

app_name = 'orders'

urlpatterns = [
    path('', include(router.urls,),),
]
