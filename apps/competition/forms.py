from django.contrib.auth import get_user_model
from django.forms import SplitDateTimeWidget
from django.contrib.admin import widgets
from apps.league.models import Competition, Team, Submit
from django import forms
from django.forms.utils import to_current_timezone


class CompetitionCreationForm(forms.ModelForm):
    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = Competition
        fields = '__all__'
        exclude = ['categories', 'owner', 'files']
        widgets = {
            'data_start_inscription': forms.SplitDateTimeWidget(),
            'data_finish_inscription': forms.SplitDateTimeWidget(),
            'data_start_competition': forms.SplitDateTimeWidget(),
            'data_finish_competition': forms.SplitDateTimeWidget(),
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
