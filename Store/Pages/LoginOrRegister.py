import unittest
from selenium.webdriver.common.by import By

class LoginOrRegisterPage(unittest.TestCase):
    LOGIN_NAME = (By.ID, 'loginFrm_loginname')
    PASSWORD = (By.ID, 'loginFrm_password')
    BTN_LOGIN = (By.CSS_SELECTOR, 'button[title="Login"]')
    BTN_REGISTER = (By.CSS_SELECTOR, 'button[title="Continue"]')
    ERROR_MSG = (By.CLASS_NAME, 'alert-error')

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(*self.LOGIN_NAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.BTN_LOGIN).click()

    def continueToRegister(self):
        self.driver.find_element(*self.BTN_REGISTER).click()

    def checkErrorMsg(self):
        return self.driver.find_element(*self.ERROR_MSG).text