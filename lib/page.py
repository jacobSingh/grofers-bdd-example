from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from component import *
from locator import *


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Home page action methods come here."""

    def __getattr__(self, key):
        if key == "shopping_cart":
            shopping_cart_elem = self.driver.find_element(*MainPageLocators.SHOPPING_CART)
            return ShoppingCartComponent(shopping_cart_elem)

    def get_first_product_card(self):
        first_product_card_elem = self.driver.find_elements(*MainPageLocators.FIRST_PRODUCT_CARD)[0]
        return ProductCardComponent(first_product_card_elem)

    def choose_city(self, city_name):
        driver = self.driver
        """Triggers the city selection"""
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(*MainPageLocators.city_button(city_name)))
        element = self.driver.find_element(*MainPageLocators.city_button(city_name))
        element.click()
        WebDriverWait(driver, 100).until(
            lambda driver: self.driver.find_element(*MainPageLocators.LOCATION_TAB).text != "Select City"
        )
