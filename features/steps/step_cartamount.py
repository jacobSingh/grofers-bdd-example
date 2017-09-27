# -*- coding: UTF-8 -*-
# MISSING-DOCSTRING: pylint: disable=C0111
"""
Based on ``my shit``

Scenario: Adding products increments the total
    Given a user is on the "/" URL
    And there is at least one product to choose
    When 1 quantity of the first product is added to cart
    Then the cart total will be equal to the price of the product

Scenario: Adding multiple products increments the total
    Given a user is on the "/" URL
    And there is at least one product to choose
    When 3 quantity of the first product is added to cart
    Then the cart total will be equal to three times the price of the product
"""

from behave import given, when, then
from hamcrest import assert_that, equal_to, is_not
import sys
import os

stupid = os.path.dirname(os.path.abspath(__file__))

sys.path.insert(0, stupid + "/../../lib")

from page import *

# @TODO: Put in an ENV var or config file (env.py)
DOMAIN = "http://grofers.com"

@given('a user is on the "{url}" URL')
def step_given_homepage(context, url):
    driver = webdriver.Safari()
    driver.set_window_size(1290, 960)
    driver.set_window_position(0,0)
    driver.get(DOMAIN + url)
    context.page = MainPage(driver)

@given('the user chooses {city} as their location')
def step_choose_city(context, city):
    context.page.choose_city(city)

@given('there is at least one product to choose')
def step_atleast_one_product(context):
    product = context.page.get_first_product_card()
    assert_that(product, is_not(None), "We have a product")

@when('{num} quantity of the first product is added to cart')
def step_product_add(context, num):
    product = context.page.get_first_product_card()
    product.add_to_cart(1)
    context.added_product_card = product

@then('the cart total will be equal to the price of the product')
def step_cart_total_should(context):
    expected_price = context.added_product_card.price
    cart_total = context.page.shopping_cart.total
    assert_that(expected_price, equal_to(cart_total))



#p = MainPage()
