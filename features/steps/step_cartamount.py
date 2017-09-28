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

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

stupid = os.path.dirname(os.path.abspath(__file__))

sys.path.insert(0, stupid + "/../../lib")

from page import MainPage

# @TODO: Put in an ENV var or config file (env.py)
DOMAIN = "http://grofers.com"

def set_up_selenium(context):
    driver = webdriver.Safari()
    driver.set_window_size(1290, 960)
    driver.set_window_position(0, 0)
    return driver

@given('a user is on the "{url}" URL')
def step_given_homepage(context, url):
    driver = set_up_selenium(context)
    context.driver = driver
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
    num = int(num)
    product = context.page.get_first_product_card()
    product.add_to_cart(num)
    context.added_product_card = product

@then('the cart total will be equal to {multiplier} times the price of the product')
def step_cart_total_should(context, multiplier):
    multiplier = int(multiplier)
    expected_price = context.added_product_card.price * multiplier

    cart_total = context.page.shopping_cart.total
    assert_that(expected_price, equal_to(cart_total))
    # THis is an anti-pattern, but it isn't closing on its own
    context.driver.quit()

@then('the title will be {expected_title}')
def step_title_assert(context, expected_title):
    assert_that(context.page.title, expected_title)
