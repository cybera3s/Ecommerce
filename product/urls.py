from django.urls import path, include
from .views import *
from .api_views import *
from .api_urls import router
app_name = 'product'

urlpatterns = [
    path('', LandingView.as_view(), name='landing'),
    path('category/<int:category_id>/<slug:category_slug>', CategoryDetailView.as_view(), name='category_detail'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    # product api urls
    path('api/', include(router.urls)),

]
