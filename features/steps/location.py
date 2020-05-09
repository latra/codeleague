from behave import *

use_step_matcher("parse")


@then(u'I\'m at "{location}"')
def step_impl(context, location):
    """
    :type location: str
    :type context: behave.runner.Context
    """
    uri = f'{context.get_url("league:home")}{location}'
    assert context.browser.url == uri
