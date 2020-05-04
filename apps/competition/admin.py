from django.contrib import admin

# Register your models here.
from apps.competition import forms
from apps.league.models import Competition


class CompetitionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Competition, CompetitionAdmin)
