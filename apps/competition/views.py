from django import http
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views import generic

from apps.account.models import LeagueUser
from apps.competition.forms import CompetitionCreationForm, TeamCreationForm
from apps.league.models import Competition, Category


class CreateCompetitionView(LoginRequiredMixin, generic.CreateView):
    login_url = reverse_lazy('account:login')
    form_class = CompetitionCreationForm
    template_name = 'competition/create.html'

    def get_success_url(self):
        return reverse_lazy('league:home')
        # return reverse_lazy('competition:detail', kwargs={'pk': self.request.user.pk})

    def form_valid(self, form):
        product = form.save(commit=False)
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


class JoinTeam(LoginRequiredMixin, generic.DetailView):
    login_url = reverse_lazy('account:login')
    template_name = 'team/join.html'
    success_url = reverse_lazy('competition:join')
    queryset = Competition.objects.all()

    def get_context_data(self, **kwargs):
        context = {}
        return super().get_context_data(**context)


class CreateTeam(LoginRequiredMixin, generic.CreateView):
    login_url = reverse_lazy('account:login')
    template_name = 'team/create.html'
    success_url = reverse_lazy('competition:create-team')
    queryset = Competition.objects.all()
    form_class = TeamCreationForm

    def get_context_data(self, **kwargs):
        context = {}
        return super().get_context_data(**context)

    def get_success_url(self):
        return reverse_lazy('league:home')
        # return reverse_lazy('competition:detail', kwargs={'pk': self.request.user.pk})

    def form_valid(self, form):
        team = form.save(commit=False)
        print(team.name)
        users = LeagueUser.objects.filter(pk=self.request.user.pk)
        team.members.add(*users)
        team.competition = Competition.objects.get(id=self.kwargs['pk'])
        return super(CreateTeam, self).form_valid(form)

class Categories(LoginRequiredMixin, generic.ListView):
    model = Category
    template_name = 'categories/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context