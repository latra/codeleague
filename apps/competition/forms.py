from django.contrib.auth import get_user_model
from django.forms import SplitDateTimeWidget
from django.contrib.admin import widgets
from apps.league.models import Competition, Team
from django import forms
from django.forms.utils import to_current_timezone


class CustomSplitDateTimeWidget(forms.MultiWidget):
    def decompress(self, value):
        if value:
            value = to_current_timezone(value)
            return [value.date(), value.time()]
        return [None, None]

    def __init__(self, attrs=None, date_format=None, time_format=None, date_attrs=None, time_attrs=None):
        widgets = (
            forms.SelectDateWidget(
                attrs=attrs if date_attrs is None else date_attrs,
            ),
            forms.TimeInput(
                attrs=attrs if time_attrs is None else time_attrs,
                format=time_format,
            ),
        )
        super().__init__(widgets)


class CompetitionCreationForm(forms.ModelForm):
    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model = Competition
        fields = '__all__'
        exclude = ['categories', 'owner', 'files']
        widgets = {
            'data_start_inscription': forms.SelectDateWidget(),
            'data_finish_inscription': forms.SelectDateWidget(),
            'data_start_competition': forms.SelectDateWidget(),
            'data_finish_competition': forms.SelectDateWidget(),
        }


class TeamCreationForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name']


class TeamJoinForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = []
        
class TeamLeaveForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = []