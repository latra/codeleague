from behave import *

use_step_matcher("parse")


@when('I visit the competition with title "{title}"')
def step_impl(context, title):
    """
    :type title: str
    :type context: behave.runner.Context
    """
    from apps.league.models import Competition
    competition = Competition.objects.get(title=title)
    context.browser.visit(context.get_url('competition:detail', competition.pk))


@then('I view all the competition information of "{title}"')
def step_impl(context, title):
    """
    :type title: str
    :type context: behave.runner.Context
    """
    from apps.league.models import Competition
    competition = Competition.objects.get(title=title)
    header = context.browser.find_by_tag('h1').first.value
    assert title == header
    description = context.browser.find_by_tag('p').first.value
    assert description == competition.description
