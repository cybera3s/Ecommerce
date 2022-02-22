from django.shortcuts import render, get_object_or_404
from django.views import View
from django.utils.translation import gettext as _
from django.views.generic import DetailView, ListView
from product.models import Category


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
