from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class LeagueUser(AbstractUser):
    github_link = models.URLField(verbose_name='GitHub Link', name='GitHub', max_length=75)
