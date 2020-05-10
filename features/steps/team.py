from behave import *


use_step_matcher("parse")


@step('Exists team "{team_name}" at competition "{title}" by "{member}"')
def step_impl(context, team_name, title, member):
    """
    :type team: str
    :type title: str
    :type member: str
    :type context: behave.runner.Context
    """
    from apps.account.models import LeagueUser
    from apps.league.models import Competition, Team
    member = LeagueUser.objects.get(username=member)
    comp = Competition.objects.get(title=title)
    team = Team.objects.create(name=team_name, competition=comp)
    team.members.add(member)
    team.save()


@then("I'm viewing a list containing all the teams of the competition")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    for i, row in enumerate(context.table):
        card = context.browser.find_by_name(f'card_team_{row["name"]}')
        print(card, f'card_team_{row["name"]}')
        assert card is not None
