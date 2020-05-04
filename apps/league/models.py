from django.db import models

# Create your models here.
from apps.account.models import LeagueUser


class Category(models.Model):
    name = models.CharField(max_length=25, unique=True)
    description = models.TextField()

    def __str__(self):
        return f'Category {self.name}'


class Competition(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    data_start_inscription = models.DateTimeField(auto_now_add=True)#null=False)
    data_finish_inscription = models.DateTimeField()#null=False)
    data_start_competition = models.DateTimeField()#null=False)
    data_finish_competition = models.DateTimeField()#null=False)
    categories = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return f'Competition {self.title}'


class Team(models.Model):
    name = models.CharField(max_length=25, unique=True)
    ranking = models.ForeignKey('Ranking', on_delete=models.CASCADE, null=True)
    members = models.ManyToManyField(LeagueUser, related_name='participants', null=True)
    competition = models.ForeignKey(Competition, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Team {self.name} in {self.competition} : {self.members.all()}'


class Ranking(models.Model):
    score = models.PositiveIntegerField(null=False, default=0)

    def __str__(self):

        return f'Ranking: {self.score}'
