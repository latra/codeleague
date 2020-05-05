from django.db import models

# Create your models here.
from django.db.models.functions import datetime
from django.utils import timezone

from apps.account.models import LeagueUser


class Category(models.Model):
    name = models.CharField(max_length=25, unique=True)
    description = models.TextField()

    def __str__(self):
        return f'Category {self.name}'


class Competition(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    owner = models.ForeignKey(LeagueUser, on_delete=models.CASCADE, null=True)
    data_start_inscription = models.DateTimeField(default=datetime.timezone.datetime.now)
    data_finish_inscription = models.DateTimeField(default=datetime.timezone.datetime.now)
    data_start_competition = models.DateTimeField(default=datetime.timezone.datetime.now)
    data_finish_competition = models.DateTimeField(default=datetime.timezone.datetime.now)
    categories = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return f'{self.title}'

    def is_inscription_opened(self):
        if self.data_start_inscription <= timezone.now() < self.data_finish_inscription:
            return True
        return False

    def is_competition_opened(self):
        if self.data_start_competition <= timezone.now() < self.data_finish_competition:
            return True
        return False


class Team(models.Model):
    name = models.CharField(max_length=25, unique=True)
    ranking = models.ForeignKey('Ranking', on_delete=models.CASCADE, null=True)
    members = models.ManyToManyField(LeagueUser, related_name='participants')
    competition = models.ForeignKey(Competition, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Team {self.name} in {self.competition} : {self.members.all()}'


class Ranking(models.Model):
    score = models.PositiveIntegerField(null=False, default=0)

    def __str__(self):
        return f'Ranking: {self.score}'
