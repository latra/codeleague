from behave import *
import operator
from functools import reduce
from django.db.models import Q

use_step_matcher("parse")


@when(u'I register a competition as "{username}"')
def step_impl(context, username):
    """
    :type username: str
    :type context: behave.runner.Context
    """
    for row in context.table:
        context.browser.visit(context.get_url('competition:createcompetition'))
        if context.browser.url == context.get_url('competition:createcompetition'):
            form = context.browser.find_by_tag('form').first
            for heading in row.headings:
                context.browser.fill(heading, row[heading])
            form.find_by_value('signup').first.click()


@then('I\'m viewing the details page for the first competition')
def step_impl(context):
    """
    :type title: str
    :type context: behave.runner.Context
    """
    q_list = [Q((attribute, context.table.rows[0][attribute])) for attribute in context.table.headings]
    from apps.league.models import Competition
    competition = Competition.objects.first()
    assert context.browser.url == context.get_url(competition)


@then(u'There are {count:n} competitions')
def step_impl(context, count):
    """
    :param count:
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And There are 1 competitions')

