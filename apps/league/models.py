from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
from django.db.models.functions import datetime
from django.utils import timezone
from django.conf import settings
from django.utils.timezone import make_aware, get_current_timezone

from apps.account.models import LeagueUser


class Category(models.Model):
    name = models.CharField(max_length=25, unique=True)
    description = models.TextField()

    def __str__(self):
        return f'Category {self.name}'


class Files(models.Model):
    title = models.CharField(max_length=50)
    file_bucket = models.CharField(max_length=255, default=None)

    @classmethod
    def create(cls, title, file_bucket):
        file_upload = cls(title=title, file_bucket=file_bucket)
        return file_upload

    def __str__(self):
        return f'Title {self.title} file{self.file_bucket}'


class Competition(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    owner = models.ForeignKey(LeagueUser, on_delete=models.CASCADE, null=True)
    data_start_inscription = models.DateTimeField(default=timezone.now)
    data_finish_inscription = models.DateTimeField()
    data_start_competition = models.DateTimeField()
    data_finish_competition = models.DateTimeField()
    categories = models.ManyToManyField(Category, blank=True)
    files = models.ManyToManyField(Files, blank=True)
    finalized = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'

    def save(self, **kwargs):
        if self.data_start_inscription < self.data_finish_inscription < self.data_finish_competition and \
                self.data_start_competition < self.data_finish_competition:
            super(Competition, self).save(**kwargs)
        else:
            raise ValidationError("Dates are not correct.")

    def is_inscription_opened(self):
        if self.data_start_inscription <= timezone.now() < self.data_finish_inscription:
            return True
        return False

    def is_competition_opened(self):
        if self.data_start_competition <= timezone.now() < self.data_finish_competition:
            return True
        return False

    def is_competition_ended(self):
        if timezone.now() > self.data_finish_inscription:
            return True
        return False


class Submit(models.Model):
    description = models.TextField()
    githuburl = models.URLField(blank=True, max_length=200)
    files = models.ManyToManyField(Files, blank=True)
    submit_date = models.DateField(auto_now=True)
    team_id = models.IntegerField(null=True)

    def __str__(self):
        return f'Submision at day ({self.submit_date})'


class Team(models.Model):
    name = models.CharField(max_length=25, unique=True)
    ranking = models.ForeignKey('Ranking', on_delete=models.CASCADE, null=True)
    members = models.ManyToManyField(LeagueUser, related_name='participants')
    competition = models.ForeignKey(Competition, on_delete=models.SET_NULL, null=True)
    submition = models.ForeignKey(Submit, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'Team {self.name} in {self.competition} : {self.members.all()}'


class Ranking(models.Model):
    score = models.PositiveIntegerField(null=False, default=0)

    def __str__(self):
        return f'Ranking: {self.score}'

    @classmethod
    def create(cls, score):
        ranking = cls(score=score)
        return ranking
