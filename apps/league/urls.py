from django.urls import path
from apps.league import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
]
