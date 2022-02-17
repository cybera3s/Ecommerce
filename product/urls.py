from django.urls import path
from .views import *
from .apis import *

app_name = 'product'

urlpatterns = [
    path('', LandingView.as_view(), name='landing'),
    path('api/product_list/', ProductListCreateApiView.as_view(), name='product_list_create_api'),
    path('api/product/<int:pk>', ProductDetailApi.as_view(), name='product_detail_api'),

]
