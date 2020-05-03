from django.urls import path, include
from django.contrib.auth.views import LoginView
from django.views.generic.base import TemplateView
from apps.league import forms, views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
]
