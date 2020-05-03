from django.shortcuts import render

# Create your views here.
from django.views import generic


class Home(generic.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['competitions'] = ['hi', 'hisda']
        return context
