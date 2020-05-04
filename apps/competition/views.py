from django import http
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views import generic

from apps.competition.forms import CompetitionCreationForm
from apps.league.models import Competition


class CreateCompetitionView(LoginRequiredMixin, generic.CreateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    form_class = CompetitionCreationForm
    template_name = 'competition/create.html'

    def form_valid(self, form):
        product = form.save(commit=False)
        product.creator = self.request.user
        product.save()
        return http.HttpResponseRedirect(self.get_success_url())


class CompetitionDetail(LoginRequiredMixin, generic.DetailView):
    login_url = reverse_lazy('account:login')
    redirect_field_name = 'redirect_to'
    context_object_name = 'competition'
    template_name = 'competition/detail.html'
    queryset = Competition.objects.all()

    def get_context_data(self, **kwargs):
        context = {}
        return super().get_context_data(**context)
