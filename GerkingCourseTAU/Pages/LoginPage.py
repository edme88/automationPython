from selenium.webdriver.common.by import By


class LoginPageLocators:
    CLOSE_ALERT = (By.CSS_SELECTOR, 'button[data-dismiss="alert"]')
    NAME_INPUT = (By.ID, 'loginFrm_loginname')
    PASSWORD_INPUT = (By.ID, 'loginFrm_password')
    LOGIN_BTN = (By.CSS_SELECTOR, 'button[title="Login"]')
    FORGOT_LOGIN_LINK = (By.CSS_SELECTOR, 'fieldset a:nth-of-type(2)')
    LASTNAME_INPUT = (By.ID, 'forgottenFrm_lastname')
    EMAIL_INPUT = (By.ID, 'forgottenFrm_email')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, 'button[title="Continue"]')
    ERROR_MSG = (By.CSS_SELECTOR, 'div.alert-danger')
    OK_MSG = (By.CSS_SELECTOR, 'div.alert-success')


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def getCloseAlert(self):
        return self.driver.find_element(*LoginPageLocators.CLOSE_ALERT)

    def getInputName(self):
        return self.driver.find_element(*LoginPageLocators.NAME_INPUT)

    def getInputPassword(self):
        return self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT)

    def getBtnLogin(self):
        return self.driver.find_element(*LoginPageLocators.LOGIN_BTN)

    def getForgotLoginLink(self):
        return self.driver.find_element(*LoginPageLocators.FORGOT_LOGIN_LINK)

    def getLastNameInput(self):
        return self.driver.find_element(*LoginPageLocators.LASTNAME_INPUT)

    def getEmailInput(self):
        return self.driver.find_element(*LoginPageLocators.EMAIL_INPUT)

    def getContinueButton(self):
        return self.driver.find_element(*LoginPageLocators.CONTINUE_BUTTON)

    def getErrorMsg(self):
        return self.driver.find_element(*LoginPageLocators.ERROR_MSG)

    def getOkMsg(self):
        return self.driver.find_element(*LoginPageLocators.OK_MSG)
