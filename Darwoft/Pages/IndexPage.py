import unittest
from selenium.webdriver.common.by import By

class IndexPage(unittest.TestCase):
    BTN_LOGIN_REGISTER = (By.CSS_SELECTOR, '#customer_menu_top > li')

    def __init__(self, driver):
        self.driver = driver

    def goToLoginOrRegisterPage(self):
        self.driver.find_element(*self.BTN_LOGIN_REGISTER).click()