from django import http
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views import generic

from apps.competition.forms import CompetitionCreationForm


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
