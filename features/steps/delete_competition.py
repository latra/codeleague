from behave import *

use_step_matcher("parse")


@when('I delete the competition with name "{title}"')
def step_impl(context, title):
    """
    :type context: str
    :type title: behave.runner.Context
    """
    from apps.league.models import Competition
    comp = Competition.objects.get(title=title)
    context.browser.visit(context.get_url('competition:detail', pk=comp.pk))
    context.browser.find_by_name(f'delete_competition').first.click()
    context.browser.visit(context.get_url('competition:delete', pk=comp.pk))
    form = context.browser.find_by_tag('form')
    if form:
        for heading in context.table.headings:
            print(heading)
            context.browser.find_by_name('confirm').first.click()

@then('I\'m viewing a list of the competitions which are still created')
def step_impl(context):
    """
    :type context: str
    """
    for i, row in enumerate(context.table):
        card = context.browser.find_by_css('div.card')
        card_title = card.find_by_css('h4.card-title')
        card_text_title = card_title.find_by_text(f'{row["title"]}')
        assert card_text_title is not None


@then(u'The list contains {count:n} competitions')
def step_impl(context, count):
    """
    :type context:
    :type count:
    """
    from apps.league.models import Competition
    assert 1 == Competition.objects.all().__len__()
