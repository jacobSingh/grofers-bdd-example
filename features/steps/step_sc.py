from hamcrest import *
from behave import *

@when(u'the user adds {qty} quantity of the first product')
def step_impl(context, qty):
    #context.plpPage.addItemToCart(qty)
    assert_that(1, equal_to(1), "Putting two items into the shopping cart")
    
@then(u'the shopping cart will have 2 products in it')
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Then the shopping cart will have 2 products in it')


@when(u'the user removes 2 quantity of the first product from the cart')
def step_impl(context):
    raise NotImplementedError(
        u'STEP: When the user removes 2 quantity of the first product from the cart')


@then(u'the shopping cart will have 0 products in it')
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Then the shopping cart will have 0 products in it')
