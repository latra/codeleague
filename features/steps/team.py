from behave import *

use_step_matcher("re")


@step('Exists team "team1" at competition "Competition1" by "user2"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
