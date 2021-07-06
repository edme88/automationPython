import unittest
from selenium.webdriver.common.by import By

class CheckoutConfirmationPage(unittest.TestCase):
    TITLE = (By.CSS_SELECTOR, 'h1')
    BTN_CONFIRM_ORDER = (By.ID, 'checkout_btn')

    def __init__(self, driver):
        self.driver = driver

    def getTitle(self):
        return self.driver.find_element(*self.TITLE).text

    def clickConfirmationBtn(self):
        self.driver.find_element(*self.BTN_CONFIRM_ORDER).click()