from behave import *

use_step_matcher("re")


@when("I list competitions")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.browser.visit(context.get_url('competition:list'))
