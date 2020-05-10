from behave import *

use_step_matcher("re")


@when("I list categories")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.browser.visit(context.get_url('category:listofcategories'))


@then("I'm viewing a list containing all the categories")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    for i, row in enumerate(context.table):
        assert row['name'] == context.browser.find_by_name('cat_name')[i].text
        assert row['description'] + '...' == context.browser.find_by_name('cat_desc')[i].text
