from django.urls import path, include
from .api_urls import router
from .views import *

app_name = 'product'

urlpatterns = [
    path('', LandingView.as_view(), name='landing'),
    path('product/<int:pk>/<slug:product_slug>', ProductDetailView.as_view(), name='product_detail'),
    path('category/<int:category_id>/<slug:category_slug>', CategoryDetailView.as_view(), name='category_detail'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    # product api urls
    path('api/', include(router.urls)),

]
