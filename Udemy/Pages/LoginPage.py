import unittest
from selenium.webdriver.common.by import By

class LoginPage(unittest.TestCase):
    USERNAME = (By.ID, 'email')
    PASSWORD = (By.ID, 'passwd')
    BTN_SUBMIT = (By.ID, 'SubmitLogin')
    FIRST_MSG_ERROR = (By.CSS_SELECTOR, 'div.alert-danger>p')
    SECOND_MSG_ERROR = (By.CSS_SELECTOR, 'div.alert-danger>ol>li')
    INPUT_CREATE_ACCOUNT = (By.ID, 'email_create')
    BTN_CREATE = (By.ID, 'SubmitCreate')
    ACCOUNT_MSG_ERROR = (By.ID, 'create_account_error')

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.BTN_SUBMIT).click()

    def checkError1(self):
        print('Text Error from UI '+self.driver.find_element(*self.FIRST_MSG_ERROR).text)
        return self.driver.find_element(*self.FIRST_MSG_ERROR).text

    def checkError2(self):
        print('Text Error from UI '+self.driver.find_element(*self.SECOND_MSG_ERROR).text)
        return self.driver.find_element(*self.SECOND_MSG_ERROR).text

    def createAccount(self, account):
        self.driver.find_element(*self.INPUT_CREATE_ACCOUNT).send_keys(account)
        self.driver.find_element(*self.BTN_CREATE).click()

    def checkError3(self):
        print('Text Error from UI ' + self.driver.find_element(*self.ACCOUNT_MSG_ERROR).text)
        return self.driver.find_element(*self.ACCOUNT_MSG_ERROR).text