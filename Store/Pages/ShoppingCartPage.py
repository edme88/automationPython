import unittest
from selenium.webdriver.common.by import By

class ShoppingCartPage(unittest.TestCase):
    BTN_CHECKOUT = (By.ID, 'cart_checkout1')
    TITLE = (By.TAG_NAME, 'h1')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product-list td.align_left a')
    PRODUCT_COLOR = (By.CSS_SELECTOR, '.product-list td.align_left a+div')
    UNIT_PRICE = (By.CSS_SELECTOR, '.product-list td.align_right:nth-of-type(4)')
    QUANTITY = (By.CSS_SELECTOR, '.product-list td.align_center input')
    TOTAL_PRICE = (By.CSS_SELECTOR, '.product-list td.align_right:nth-of-type(6)')

    def __init__(self, driver):
        self.driver = driver

    def checkTitle(self):
        return self.driver.find_element(*self.TITLE).text

    def clickCheckout(self):
        self.driver.find_element(*self.BTN_CHECKOUT).click()

    def checkProductName(self):
        return self.driver.find_element(*self.PRODUCT_NAME).text

    def checkProductColor(self):
        return self.driver.find_element(*self.PRODUCT_COLOR).text

    def checkProductUnitPrice(self):
        return self.driver.find_element(*self.UNIT_PRICE).text

    def checkProductQuantity(self):
        return self.driver.find_element(*self.QUANTITY).get_attribute('value')

    def checkProductTotalPrice(self):
        return self.driver.find_element(*self.TOTAL_PRICE).text