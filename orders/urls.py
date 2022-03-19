from django.urls import path, include
from .api_urls import router
from .api_views import CartItemApiView
from .views import CartCheckOutView, PaymentView


app_name = 'orders'

urlpatterns = [
    path('api/', include(router.urls,),),
    path('api/cart_item/', CartItemApiView.as_view(), name='cart_item_api'),
    path('api/cart_item/<pk>', CartItemApiView.as_view(), name='detail_cart_item_api'),
    path('api/cart_item/<pk>/', CartItemApiView.as_view(), name='delete_cart_item'),
    path('api/cart_item/<pk>/', CartItemApiView.as_view(), name='update_cart_item'),

    path('cart/checkout/', CartCheckOutView.as_view(), name='cart_checkout'),
    path('cart/payment/', PaymentView.as_view(), name='cart_payment'),
]
