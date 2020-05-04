from apps.league.models import Competition

# Create your views here.
from django.views import generic


class Home(generic.ListView):
    model = Competition
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
class Info(generic.ListView):
    template_name = 'info.html'


