from django.contrib.auth import get_user_model
from apps.league.models import Competition
from django import forms


class CompetitionCreationForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = ('title',
                  'description',
                  'data_start_inscription',
                  'data_finish_inscription',
                  'data_start_competition',
                  'data_finish_competition',
                  'categories',
                  )
