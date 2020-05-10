from behave import *

use_step_matcher("parse")


@when('I join team "{team_name}" at competition "{title}"')
def step_impl(context, team_name, title):
    """
    :type team_name: str
    :type title: str
    :type context: behave.runner.Context
    """
    from apps.league.models import Team, Competition
    comp = Competition.objects.get(title=title)
    context.browser.visit(context.get_url('competition:detail', pk=comp.pk))
    team = Team.objects.get(name=team_name)
    print(context.browser.html)
    print(context.browser.find_by_name(f'members'))
    print(context.browser.find_by_name(f'join'))
    assert context.browser.find_by_name(f'members')[0].text == "1/4 members"
    context.browser.find_by_name(f'join').first.click()


@then('There are {count:n} members at team "{team_name}" at competition "{title}"')
def step_impl(context, count, team_name, title):
    """
    :type team1: str
    :type title: str
    :type count: str
    :type context: behave.runner.Context
    """
    from apps.league.models import Team, Competition
    comp = Competition.objects.get(title=title)
    context.browser.visit(context.get_url('competition:detail', pk=comp.pk))
    assert context.browser.find_by_name(f'members')[0].text == "2/4 members"


@when('I want to join at competition "{title}"')
def step_impl(context, title):
    """
    :type team_name: str
    :type title: str
    :type context: behave.runner.Context
    """
    from apps.league.models import Team, Competition
    comp = Competition.objects.get(title=title)
    context.browser.visit(context.get_url('competition:detail', pk=comp.pk))