from behave import *

use_step_matcher("parse")


@step('Exists a category "{name}" with description "{desc}"')
def step_impl(context, name, desc):
    """
    :type name: str
    :type desc: str
    :type context: behave.runner.Context
    """
    from apps.league.models import Category
    Category.objects.create(name=name, description=desc)
