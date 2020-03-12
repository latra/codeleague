from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import LeagueUser, Category, Competition, Ranking, Team


class CategoryAdmin(admin.ModelAdmin):
    pass


class CompetitionAdmin(admin.ModelAdmin):
    pass


class RankingAdmin(admin.ModelAdmin):
    pass


class TeamAdmin(admin.ModelAdmin):
    pass


admin.site.register(LeagueUser, UserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Competition, CompetitionAdmin)
admin.site.register(Ranking, RankingAdmin)
admin.site.register(Team, TeamAdmin)
