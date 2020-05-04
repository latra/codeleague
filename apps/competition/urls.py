from django.urls import path
from apps.competition import views
from apps.competition.apps import CompetitionConfig

app_name='competition'
urlpatterns = [
    path('create/', views.CreateCompetitionView.as_view(), name='createcompetition'),
    path('id/<int:pk>', views.CompetitionDetail.as_view(), name='detail'),
]
