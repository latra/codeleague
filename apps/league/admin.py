from django.contrib import admin
from .models import Category, Competition, Ranking, Team


class CategoryAdmin(admin.ModelAdmin):
    pass


class RankingAdmin(admin.ModelAdmin):
    pass


class TeamAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(Ranking, RankingAdmin)
admin.site.register(Team, TeamAdmin)
