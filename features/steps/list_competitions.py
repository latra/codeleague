from behave import *

use_step_matcher("parse")


@when("I list competitions")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.browser.visit(context.get_url('competition:list'))


@then("I'm viewing a list containing all the competitions")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    for row in context.table:
        context.browser.find_by_css('card').find_by_css('card-title').find_by_text(f'{row["title"]}')


@step(u'The list contains {count:n} competitions')
def step_impl(context, count):
    """
    :type count: str
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And The list contains 7 competitions')
