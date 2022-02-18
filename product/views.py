from django.shortcuts import render
from django.views import View
from django.utils.translation import gettext as _


class LandingView(View):
    template_name = 'product/landing.html'

    def get(self, request):
        data = {
            'title': _('landing')
        }
        return render(request, self.template_name, data)
