from django.urls import path, include
from .api_urls import router
from .api_views import AddToCartApiView
from .views import CartCheckOutView


app_name = 'orders'

urlpatterns = [
    path('api/', include(router.urls,),),
    path('api/cart_item/', AddToCartApiView.as_view(), name='add_to_cart_api'),
    path('checkout/cart/', CartCheckOutView.as_view(template_name='orders/cart/cart.html'), name='cart_checkout'),
]
