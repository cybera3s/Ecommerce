from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.utils.translation import gettext as _
from django.views.generic import DetailView, ListView, TemplateView

from comments.forms import CommentCreateForm
from product.models import Category, Product


class LandingView(TemplateView):
    template_name = 'product/landing/landing.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('landing')
        return context


class CategoryListView(ListView):
    model = Category
    template_name = 'product/category/category_list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        categories = Category.objects.filter(root=None)
        return categories


class CategoryDetailView(View):
    template_name = 'product/category/category_detail.html'

    def setup(self, request, *args, **kwargs):
        self.category_instance = get_object_or_404(Category, pk=kwargs['category_id'], slug=kwargs['category_slug'])
        return super().setup(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        data = {
            'title': self.category_instance.name,
            'category_id': self.kwargs['category_id']
        }

        return render(request, self.template_name, data)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_detail.html'
    context_object_name = 'product'
    form_class = CommentCreateForm

    def setup(self, request, *args, **kwargs):
        self.product_instance = get_object_or_404(Product, pk=kwargs['pk'], slug=kwargs['product_slug'])
        return super().setup(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        comments = self.product_instance.pcomments.filter(is_reply=False, can_publish=True)
        context['comments'] = comments
        context['comment_form'] = self.form_class
        return self.render_to_response(context)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user.customer
            request.user.first_name = form.cleaned_data['name']
            request.user.save()
            new_comment.product = self.product_instance
            new_comment.save()
            return redirect('product:product_detail', self.product_instance.id, self.product_instance.slug)
