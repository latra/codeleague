from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from apps.league.models import Category, Competition

# Create your views here.
from django.views import generic


class ListCategories(LoginRequiredMixin, generic.ListView):
    model = Category
    template_name = 'list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['competitions'] = {}
        for category in context['object_list']:
            context['competitions'][category.id] = Competition.objects.filter(categories=category)
        return context
