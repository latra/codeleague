from behave import *

use_step_matcher("parse")


@when('I visit profile of "{username}"')
def step_impl(context, username):
    """
    :type username: str
    :type context: behave.runner.Context
    """
    from apps.account.models import LeagueUser
    user = LeagueUser.objects.all().get(username=username)
    context.browser.visit(context.get_url('account:user_detail', pk=user.id))


@then('I view profile of "{username}" information')
def step_impl(context, username):
    """
    :type username: str
    :type context: behave.runner.Context
    """
    from apps.account.models import LeagueUser
    user = LeagueUser.objects.all().get(username=username)
    assert context.browser.find_by_tag('h1').find_by_text(user.username) is not None