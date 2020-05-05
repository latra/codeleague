from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from apps.league.models import Category, Competition

# Create your views here.
from django.views import generic


class ListCategories(LoginRequiredMixin, generic.ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'category_home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['competitions'] = {}
        for category in context['object_list']:
            context['competitions'][category.id] = Competition.objects.filter(categories=category)
        return context


class SearchCategories(LoginRequiredMixin, generic.TemplateView):
    context_object_name = 'context'
    template_name = 'cat_search.html'

    def get_context_data(self, **kwargs):
        query = self.request.GET.get('q')
        categories = Category.objects.filter(name__contains=query).union(
            Category.objects.filter(description__contains=query))
        context = {'query': query, 'categories': categories, 'competitions': {}}
        for category in categories:
            context['competitions'][category.id] = Competition.objects.filter(categories=category)
        return context
