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
    for i, row in enumerate(context.table):
        card = context.browser.find_by_css('div.card')
        card_title = card.find_by_css('h4.card-title')
        card_text_title = card_title.find_by_text(f'{row["title"]}')
        assert card_text_title is not None


@step(u'The list contains {count:n} competitions')
def step_impl(context, count):
    """
    :type count: str
    :type context: behave.runner.Context
    """
    cards = context.browser.find_by_css('div.card')
    assert len(cards) == count
