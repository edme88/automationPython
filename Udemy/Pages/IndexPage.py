import unittest
from selenium.webdriver.common.by import By

class IndexPage(unittest.TestCase):
    LOGIN_BUTTON = (By.CLASS_NAME, 'login')

    def __init__(self, driver):
        self.driver = driver

    def goToLoginPage(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()