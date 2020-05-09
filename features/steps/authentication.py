from behave import *

use_step_matcher("parse")


@given('Exists a user "{username}" with password "{password}"')
def step_impl(context, username, password):
    """
    :type username: str
    :type password: str
    :type context: behave.runner.Context
    """
    from apps.account.models import LeagueUser as User
    User.objects.create_user(username=username, email='user@example.com', password=password)


@given('I login as user "{username}" with password "{password}"')
def step_impl(context, username, password):
    """
    :type username: str
    :type password: str
    :type context: behave.runner.Context
    """
    context.browser.visit(context.get_url('/accounts/login/?next=/'))
    form = context.browser.find_by_tag('form').first
    context.browser.fill('username', username)
    context.browser.fill('password', password)
    form.find_by_value('login').first.click()
    assert context.browser.is_text_present('COMPETITIONS')


@given('I\'m not logged in')
def step_impl(context):
    context.browser.visit(context.get_url('account:logout'))
    assert context.browser.url == context.get_url('league:home')


@then('Need to login to have "{path}" link available')
def step_impl(context, path):
    """
    :type path: str
    :type context: behave.runner.Context
    """
    uri = context.get_url('account:login') + f'?next=/{path}'
    assert context.browser.url == uri

