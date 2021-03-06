from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import re
from locator import *

class BasePageComponent(object):
    def __init__(self, element):
        self.element = element

class ProductCardComponent(BasePageComponent):
    """ @TODO: Implement multi quantity """
    def __getattr__(self, key):
        driver = self.element
        if key == "price":
            price = driver.find_element(*ProductCardLocators.PRICE)
            # @TODO: Consider multi-currency support and decimal
            return int(re.sub(r'[^\d]', '', price.text))


    def add_to_cart(self, qty):
        driver = self.element
        WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element(*ProductCardLocators.ADD_BUTTON))

        add_button = driver.find_element(*ProductCardLocators.ADD_BUTTON)
        add_button.click()

        def is_int(x):
            try:
                float(x)
                return True
            except(ValueError):
                return False
            except(TypeError):
                return False

        WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element(*ProductCardLocators.QUANTITY_SELECTOR).text != "Add To Cart")

        def get_current_qty():
            driver = self.element
            return int(driver.find_element(*ProductCardLocators.QUANTITY_SELECTOR).text)

        while qty > get_current_qty():
            current_qty = get_current_qty()
            WebDriverWait(driver, 10).until(
                lambda driver: driver.find_element(*ProductCardLocators.PLUS_BUTTON))
            plus_button = driver.find_element(*ProductCardLocators.PLUS_BUTTON)
            plus_button.click()
            WebDriverWait(driver, 10).until(
                lambda x: current_qty != get_current_qty())

class ShoppingCartComponent(BasePageComponent):
    def __getattr__(self, key):
        driver = self.element
        if key == "total":
            total = driver.find_element(*ShoppingCartLocators.TOTAL)
            # @TODO: Consider multi-currency support and decimal
            return int(re.sub(r'[^\d]', '', total.text))
