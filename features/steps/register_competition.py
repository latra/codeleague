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
            context.browser.find_by_name('create').first.click()


@then('I\'m viewing the details page for the first competition')
def step_impl(context):
    """
    :type title: str
    :type context: behave.runner.Context
    """
    from apps.league.models import Competition
    q_list = [Q((attribute, context.table.rows[0][attribute])) for attribute in context.table.headings]
    competition = Competition.objects.first()
    assert context.browser.url == context.get_url('competition:detail', pk=competition.id)


@then(u'There are {count:n} competitions')
def step_impl(context, count):
    """
    :param count:
    :type context: behave.runner.Context
    """
    from apps.league.models import Competition
    assert 1 == Competition.objects.all().__len__()


@when(u'I want to register a competition')
def step_impl(context):
    """
    :type username: str
    :type context: behave.runner.Context
    """
    context.browser.visit(context.get_url('competition:createcompetition'))
    print(context.browser.url)
    assert context.browser.url != context.get_url('competition:createcompetition')
