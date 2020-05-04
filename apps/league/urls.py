from django.urls import path
from apps.league import views

app_name='league'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('info/', views.Info.as_view(), name='info'),
]
