from product.models import Category


def access_category_items(request):
    """
      The context processor to access categories in all pages
    """
    categories = Category.objects.all()
    return {'nav_categories': categories}
