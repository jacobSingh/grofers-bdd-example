from hamcrest import *
from behave import *

@given(u'a user is on a {category} category page')
def step_impl(context, category):
    assert_that(1, equal_to(1), "Navigating to a category")


@when(u'the user goes to the shopping cart')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user goes to the shopping cart')
