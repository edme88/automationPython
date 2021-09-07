import unittest
from selenium.webdriver.common.by import By

class ConfirmationPage(unittest.TestCase):
    TITLE = (By.CSS_SELECTOR, 'h1')

    def __init__(self, driver):
        self.driver = driver

    def getTitle(self):
        return self.driver.find_element(*self.TITLE).text