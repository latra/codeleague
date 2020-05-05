from django.urls import path
from apps.competition import views
from apps.competition.apps import CompetitionConfig

app_name = 'competition'
urlpatterns = [
    path('create/', views.CreateCompetitionView.as_view(), name='createcompetition'),
    path('id/<int:pk>/', views.CompetitionDetail.as_view(), name='detail'),
    path('id/<int:pk>/edit/', views.CompetitionUpdate.as_view(), name='edit'),
    path('id/<int:pk>/create-team/', views.CreateTeam.as_view(), name='create-team'),
    path('search/', views.SearchCompetitions.as_view(), name="search"),
]
