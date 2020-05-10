from behave import *

use_step_matcher("parse")


@then(u'I\'m at "{location}"')
def step_impl(context, location):
    """
    :type location: str
    :type context: behave.runner.Context
    """
    uri = f'{context.get_url("league:home")}{location}'
    print(context.browser.url, uri)
    assert context.browser.url == uri


@when('I am at "{reverse}" page')
def step_impl(context, reverse):
    """
    :type reverse: str
    :type context: behave.runner.Context
    """
    context.browser.visit(context.get_url(reverse))