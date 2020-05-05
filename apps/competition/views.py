from django import http
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views import generic

from apps.competition.forms import CompetitionCreationForm, TeamCreationForm, TeamJoinForm, TeamLeaveForm
from apps.league.models import Team, Competition, Category
from apps.competition.forms import CompetitionCreationForm, TeamCreationForm, TeamJoinForm
from apps.league.models import Team, Competition


class CreateCompetitionView(LoginRequiredMixin, generic.CreateView):
    login_url = reverse_lazy('account:login')
    form_class = CompetitionCreationForm
    template_name = 'competition/create.html'

    def get_success_url(self):
        return reverse_lazy('league:home')
        # return reverse_lazy('competition:detail', kwargs={'pk': self.request.user.pk})

    def form_valid(self, form):
        competition = form.save(commit=False)
        competition.owner = self.request.user
        competition.save()
        return http.HttpResponseRedirect(self.get_success_url())


class CompetitionUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Competition
    fields = ['title', 'description']
    template_name = 'competition/competition_update_form.html'

    def get_context_data(self, **kwargs):
        context = {}
        return super().get_context_data(**context)

    def test_func(self):
        competition = Competition.objects.get(pk=self.kwargs['pk'])
        return competition.owner.pk == self.request.user.pk

    def get_success_url(self):
        return reverse_lazy('league:home')


class CompetitionDetail(LoginRequiredMixin, generic.DetailView, generic.CreateView):
    login_url = reverse_lazy('account:login')
    redirect_field_name = 'redirect_to'
    context_object_name = 'competition'
    template_name = 'competition/detail.html'
    success_url = reverse_lazy('competition:join-team')
    form_class = TeamJoinForm

    queryset = Competition.objects.all()

    def get_context_data(self, **kwargs):
        context = {}
        context['user'] = self.request.user
        context['groups'] = Team.objects.filter(competition=self.kwargs.get(self.pk_url_kwarg))
        context['haveTeam'] = False
        for group in context['groups']:
            if context['user'] in group.members.all():
                context['haveTeam'] = True

        context.update(kwargs)
        return super().get_context_data(**context)

    def form_valid(self, form):
        competition = Competition.objects.filter(id=self.kwargs['pk'])[0]
        action = self.request.POST.get('action')
        if competition.is_inscription_opened():
            team = Team.objects.filter(id=self.request.POST.get('teamId'))[0]
            if action == 'join':
                team.members.add(self.request.user.pk)
                team.save()
            elif action == 'leave':
                team.members.remove(self.request.user.pk)
                team.save()
                if len(team.members.all()) == 0:
                    team.delete()
            return http.HttpResponseRedirect(self.get_success_url())
        return http.HttpResponseForbidden()

    def get_success_url(self):
        return reverse_lazy('competition:detail', kwargs={'pk': self.kwargs['pk']})


class CreateTeam(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    login_url = reverse_lazy('account:login')
    template_name = 'team/create.html'
    success_url = reverse_lazy('competition:create-team')
    queryset = Competition.objects.all()
    form_class = TeamCreationForm

    def get_context_data(self, **kwargs):
        context = {}

        return super().get_context_data(**context)

    def get_success_url(self):
        return reverse_lazy('competition:detail', kwargs={'pk': self.kwargs['pk']})

    def test_func(self):
        competition = Competition.objects.filter(id=self.kwargs.get(self.pk_url_kwarg))[0]
        if competition.owner == self.request.user:
            return False
        teams = Team.objects.filter(competition=self.kwargs.get(self.pk_url_kwarg))
        for team in teams:
            if self.request.user in team.members.all():
                return False
        return True

    def form_valid(self, form):
        team = form.save(commit=False)
        team.competition = Competition.objects.get(pk=self.kwargs['pk'])
        team.save()
        team.members.add(self.request.user.pk)
        team.save()
        return http.HttpResponseRedirect(self.get_success_url())


class SearchCompetitions(LoginRequiredMixin, generic.TemplateView):
    context_object_name = 'context'
    template_name = 'search/list.html'

    def get_context_data(self, **kwargs):
        query = self.request.GET.get('q')
        competitions = Competition.objects.filter(title__contains=query).union(
            Competition.objects.filter(description__contains=query))
        context = {'query': query, 'competitions': competitions}
        return context
