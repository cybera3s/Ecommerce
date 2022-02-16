from django.shortcuts import render
from django.views import View


class LandingView(View):
    template_name = 'product/landing.html'

    def get(self, request):
        return render(request, self.template_name)
