from django.urls import path, include
from .api_urls import router
from .api_views import AddToCartApiView


app_name = 'orders'

urlpatterns = [
    path('api/', include(router.urls,),),
    path('add_to_cart_api/', AddToCartApiView.as_view(), name='add_to_cart_api'),
]
