from django.shortcuts import redirect
from django.urls import URLResolver, URLPattern


# LOGIN_EXEMPT_URLS = [
#     '/',
#     '/en/',
#     '/en/customers/login/',
#     '/media/',
#     '/static/',
#     '/en/api/',
#     '/en/rosetta/',
#     '/en/customers/register/',
#     '/locale/',
#     '/orders/',
#     '/category/',
#     '/product/',
#     '/en/api/products/',
#     '/en/api/brands/'
#
# ]

LOGIN_REQUIRED_URLS = [
    # '/en/categories/'
]


class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and (request.path in LOGIN_REQUIRED_URLS):
            return redirect('customers:customer_login')

        response = self.get_response(request)

        return response
