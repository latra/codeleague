from django import http
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from apps.competition.forms import CompetitionCreationForm


class CreateCompetitionView(generic.CreateView, LoginRequiredMixin):
    form_class = CompetitionCreationForm
    template_name = 'competition/create.html'

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.request.user.pk})

    def form_valid(self, form):
        product = form.save(commit=False)
        product.creator = self.request.user
        product.save()
        return http.HttpResponseRedirect(self.get_success_url())
