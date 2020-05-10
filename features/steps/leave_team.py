
from behave import *

use_step_matcher("parse")


@when('I leave team "{team_name}" at competition "{title}"')
def step_impl(context, team_name, title):
    """
    :type team_name: str
    :type competition: str
    :type context: behave.runner.Context
    """
    from apps.league.models import Team, Competition
    from time import sleep

    comp = Competition.objects.get(title=title)
    context.browser.visit(context.get_url('competition:detail', pk=comp.pk))
    context.browser.find_by_name(f'leave_group').first.click()
    sleep(1) # Needed because the modal has to be visible.
    context.browser.find_by_name('confirm_leave').first.click()


@then('There are {cont:n} teams at competition "{title}"')
def step_impl(context, cont, title):
    """
    :type cont: str
    :type title: str
    :type context: behave.runner.Context
    """
    from apps.league.models import Team, Competition
    comp = Competition.objects.get(title=title)
    teams = Team.objects.all().filter(competition=comp)
    print(teams)
    for team in teams:
        print(team.members)
    assert len(teams.all()) == 0


@when('I want to leave at competition "{title}"')
def step_impl(context, title):
    """
    :type team_name: str
    :type title: str
    :type context: behave.runner.Context
    """
    from apps.league.models import Team, Competition
    comp = Competition.objects.get(title=title)
    context.browser.visit(context.get_url('competition:detail', pk=comp.pk))