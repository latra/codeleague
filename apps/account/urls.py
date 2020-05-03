from django.urls import path, include
from django.contrib.auth.views import LoginView
from django.views.generic.base import TemplateView
from apps.account import forms, views

app_name='account'
urlpatterns = [
    path('login/', LoginView.as_view(authentication_form=forms.AuthenticationForm), name='login'),
    path('signup/', views.SignUp.as_view(), name='sign-up'),
    path('', include('django.contrib.auth.urls')),
    path('u/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
]
