import unittest
from selenium.webdriver.common.by import By

class MyAccountPage(unittest.TestCase):
    USERNAME = (By.CSS_SELECTOR, 'a.account')

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.find_element(*self.USERNAME).text