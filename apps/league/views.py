from apps.league.models import Competition

# Create your views here.
from django.views import generic


class Home(generic.ListView):
    model = Competition
    context_object_name = 'competitions'
    template_name = 'home.html'

    def get_queryset(self, *args, **kwargs):
        return filter(lambda x: x.is_inscription_opened(), self.model.objects.all().order_by('data_finish_competition'))


class Info(generic.TemplateView):
    template_name = 'info.html'
