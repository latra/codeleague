from django.urls import path
from apps.competition import views

urlpatterns = [
    path('create/', views.CreateCompetitionView.as_view(), name='creat-competition'),
]
