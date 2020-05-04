from django.contrib.auth import get_user_model
from django.forms import SplitDateTimeWidget
from django.contrib.admin import widgets
from apps.league.models import Competition
from django import forms


class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'


class CompetitionCreationForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = '__all__'
        exclude = ['categories']
        widgets = {
            'data_start_inscription': forms.SelectDateWidget(),
            'data_finish_inscription': forms.SelectDateWidget(),
            'data_start_competition': forms.SelectDateWidget(),
            'data_finish_competition': forms.SelectDateWidget(),
        }
