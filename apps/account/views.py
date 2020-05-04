from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import DetailView

from apps.account.forms import UserCreationForm, AuthenticationForm
from apps.account.models import LeagueUser


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('account:login')
    template_name = 'sign_up.html'


# We are using reverse_lazy because for all generic class-based views the urls
# are not loaded when the file is imported, so we have to use the lazy form of
# reverse to load them later when they are available.

class UserDetail(LoginRequiredMixin, DetailView):
    template_name = "account.html"
    context_object_name = 'user'
    model = LeagueUser

    def get_context_data(self, **kwargs):
        context = super(UserDetail, self).get_context_data(**kwargs)
        return context


class Login(LoginView):
    authentication_form = AuthenticationForm
    success_url = reverse_lazy('account:login')
    redirect_field_name = 'redirect_to'

