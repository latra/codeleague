from django.contrib.auth import get_user_model
from apps.league.models import Competition
from django import forms


class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'


class CompetitionCreationForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = '__all__'
        widgets = {
            'data_start_inscription': DateTimeInput(),
            'data_finish_inscription': DateTimeInput(),
            'data_start_competition': DateTimeInput(),
            'data_finish_competition': DateTimeInput(),
        }
