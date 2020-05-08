from django.contrib.auth import get_user_model
from django.forms import SplitDateTimeWidget
from django.contrib.admin import widgets
from apps.league.models import Competition, Team, Submit
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
    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)
    class Meta:
        model = Competition
        fields = '__all__'
        exclude = ['categories', 'owner', 'files']
        widgets = {
            'data_start_inscription': forms.SelectDateWidget(),
            'data_finish_inscription': forms.SelectDateWidget(),
            'data_start_competition': forms.SelectDateWidget(),
            'data_finish_competition': forms.SelectDateWidget(),
            'hour_start_inscription': forms.TimeInput(),
            'hour_finish_inscription': forms.TimeInput(),
            'hour_start_competition': forms.TimeInput(),
            'hour_finish_competition': forms.TimeInput(),
        }


class TeamCreationForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name']


class TeamJoinForm(forms.ModelForm):
    action = forms.CharField(max_length=30, required=False)
    class Meta:
        model = Team
        fields = []
class DownloadFile(forms.ModelForm):
    action = forms.CharField(max_length=30, required=False)
    class Meta:
        model = Competition
        fields = []
class TeamLeaveForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = []

class PublishAnswerForm(forms.ModelForm):
    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)
    class Meta:
        model = Submit
        fields = '__all__'
        exclude = ['files', 'team_id']
