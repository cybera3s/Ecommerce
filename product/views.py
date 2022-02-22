from django.shortcuts import render, get_object_or_404
from django.views import View
from django.utils.translation import gettext as _
from django.views.generic import DetailView, ListView
from product.models import Category, Product


class LandingView(View):
    template_name = 'product/landing.html'

    def get(self, request):
        data = {
            'title': _('landing')
        }
        return render(request, self.template_name, data)


class CategoryListView(ListView):
    model = Category
    template_name = 'product/category/category_list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        categories = Category.objects.all().exclude(root=None)
        return categories


class CategoryDetailView(View):
    template_name = 'product/category/category_detail.html'

    def setup(self, request, *args, **kwargs):
        self.category_instance = get_object_or_404(Category, pk=kwargs['category_id'])
        return super().setup(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        data = {
            'title': self.category_instance.name
        }
        category = self.category_instance
        data['products'] = Product.objects.filter(category=category)

        return render(request, self.template_name, data)
