import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class ProductPage(unittest.TestCase):
    COLOR = (By.ID, 'option305')
    QTY = (By.ID, 'product_quantity')
    BTN_CART = (By.CLASS_NAME, 'cart')
    PRODUCT_TITLE = (By.TAG_NAME, 'h1')
    UNIT_PRICE = (By.CLASS_NAME, 'productprice')
    TOTAL_PRICE = (By.CSS_SELECTOR, '.total-price-holder span')

    def __init__(self, driver):
        self.driver = driver

    def changeColor(self, color):
        self.driver.find_element(*self.COLOR).send_keys(color)

    def changeQty(self, qty):
        self.driver.find_element(*self.QTY).send_keys(Keys.BACKSPACE)
        self.driver.find_element(*self.QTY).send_keys(qty)

    def clickCart(self):
        self.driver.find_element(*self.BTN_CART).click()

    def checkTitle(self):
        return self.driver.find_element(*self.PRODUCT_TITLE).text

    def checkUnitPrice(self, price):
        assert price in self.driver.find_element(*self.UNIT_PRICE).text

    def checkTotalPrice(self, price):
        assert price in self.driver.find_element(*self.TOTAL_PRICE).text