from selenium.webdriver.common.by import By


class LoginPageLocators():
    NAME_INPUT = (By.ID, 'loginFrm_loginname')
    PASSWORD_INPUT = (By.ID, 'loginFrm_password')
    LOGIN_BTN = (By.CSS_SELECTOR, 'button[title="Login"]')


class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    def getInputName(self):
        return self.driver.find_element(*LoginPageLocators.NAME_INPUT)

    def getInputPassword(self):
        return self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT)

    def getBtnLogin(self):
        return self.driver.find_element(*LoginPageLocators.LOGIN_BTN)
