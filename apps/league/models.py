from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class LeagueUser(AbstractUser):
    github_link = models.URLField(verbose_name='GitHub Link', name='GitHub', max_length=75)


class Category(models.Model):
    name = models.CharField(max_length=25, unique=True)
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'


class Competition(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    data_start_inscription = models.DateTimeField(null=False)
    data_finish_inscription = models.DateTimeField(null=False)
    data_start_competition = models.DateTimeField(null=False)
    data_finish_competition = models.DateTimeField(null=False)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return f'{self.title}'


class Team(models.Model):
    name = models.CharField(max_length=25, unique=True)
    ranking = models.ForeignKey('Ranking', on_delete=models.CASCADE)
    members = models.ManyToManyField(LeagueUser, related_name='participants')


class Ranking(models.Model):
    #team = models.ForeignKey(Team, on_delete=models.CASCADE)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(null=False, default=0)
