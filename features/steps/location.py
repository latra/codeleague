from behave import *

use_step_matcher("parse")


@then('I\'m at "{location}"')
def step_impl(context, location):
    """
    :type location: str
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then I\'m at "competition/create/"')