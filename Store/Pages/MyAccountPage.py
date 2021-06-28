import unittest
from selenium.webdriver.common.by import By

class MyAccountPage(unittest.TestCase):
    TITLE = (By.CSS_SELECTOR, 'h1 span.maintext')

    def __init__(self, driver):
        self.driver = driver

    def checkTitle(self):
        return self.driver.find_element(*self.TITLE).text