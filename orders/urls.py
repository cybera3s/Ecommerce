from django.urls import path, include
from .api_urls import router
from .views import AddToCartView

app_name = 'orders'

urlpatterns = [
    path('api/', include(router.urls,),),
    path('add_to_cart/', AddToCartView.as_view(), name='add_to_cart')
]
