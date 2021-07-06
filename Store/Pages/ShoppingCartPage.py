import unittest
from selenium.webdriver.common.by import By

class ShoppingCartPage(unittest.TestCase):
    BTN_CHECKOUT = (By.ID, 'cart_checkout1')

    def __init__(self, driver):
        self.driver = driver

    def clickCheckout(self):
        return self.driver.find_element(*self.BTN_CHECKOUT).click()