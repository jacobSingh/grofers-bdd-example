from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    GO_BUTTON = (By.ID, 'submit')
    FIRST_PRODUCT_CARD = (By.CLASS_NAME, "product__wrapper")
    LOCATION_TAB = (By.XPATH, '//div[@data-test-id="location-tab"]')
    SHOPPING_CART = (By.CLASS_NAME, "shopping-cart")

    @classmethod
    def city_button(cls, city_name):
        return (By.XPATH, '//div[text()="{}"]'.format(city_name))

class ProductCardLocators(object):
    ADD_BUTTON = (By.XPATH, './/button[@data-test-id="add-button"]')
    QUANTITY_SELECTOR = (By.XPATH, './/button[@data-test-id="add-button"]')
    PLUS_BUTTON = (By.XPATH, './/button[@data-test-id="plus-button"]')
    PRICE = (By.CLASS_NAME, 'plp-product__price--new')

class ShoppingCartLocators(object):
    TOTAL = (By.CLASS_NAME, 'item-cart-total')
