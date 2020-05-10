from behave import *

use_step_matcher("parse")


@when('I list all competitions of category "{name}"')
def step_impl(context, name):
    """
    :type name: str
    :type context: behave.runner.Context
    """
    context.browser.visit(context.get_url('category:listofcategories'))
    context.browser.find_by_name(name).find_by_name('see_competitions').click()
    from time import sleep
    sleep(1)


@then('I\'m viewing a list containing all the competitions from category "{name}"')
def step_impl(context, name):
    """
    :type name: str
    :type context: behave.runner.Context
    """
    from apps.league.models import Competition, Category
    cat = Category.objects.get(name=name)
    competitions = Competition.objects.all().filter(categories=cat)
    for c in competitions:
        assert not context.browser.find_by_name(f'{name}_{c.title}').is_empty()
