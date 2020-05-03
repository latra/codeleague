from django.shortcuts import render
from apps.league.models import Competition

# Create your views here.
from django.views import generic

print("hi")
class Home(generic.ListView):
    model = Competition
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context
