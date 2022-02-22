from django.urls import path
from .views import *
from .api_views import *

app_name = 'product'

urlpatterns = [
    path('', LandingView.as_view(), name='landing'),
    path('category/<int:category_id>/', CategoryDetailView.as_view(), name='category_detail'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('api/product_list/', ProductListCreateApiView.as_view(), name='product_list_create_api'),
    path('api/brand_list/', BrandListCreateApiView.as_view(), name='brand_list_create_api'),
    path('api/product/<int:pk>', ProductDetailApi.as_view(), name='product_detail_api'),

]
