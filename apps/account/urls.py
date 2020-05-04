from django.urls import path, include
from django.contrib.auth.views import LoginView
from django.views.generic.base import TemplateView
from apps.account import forms, views

app_name='account'
urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('', include('django.contrib.auth.urls')),
    path('u/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
]
