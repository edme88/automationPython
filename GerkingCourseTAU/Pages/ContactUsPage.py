from selenium.webdriver.common.by import By


class ContactUsPageLocators():
    CONFIRMATION_TEXT = (By.CSS_SELECTOR, 'section.mb40 p:nth-of-type(2)')
    NAME_INPUT = (By.ID, 'ContactUsFrm_first_name')
    NAME_ERROR = (By.CSS_SELECTOR, '#field_11 .element_error')
    EMAIL_INPUT = (By.ID, 'ContactUsFrm_email')
    EMAIL_ERROR = (By.CSS_SELECTOR, '#field_12 .element_error')
    TEXT_INPUT = (By.ID, 'ContactUsFrm_enquiry')
    TEXT_ERROR = (By.CSS_SELECTOR, '#field_13 .element_error')
    SUBMIT_BTN = (By.CSS_SELECTOR, 'button[title="Submit"]')

class ContactUsPage():

    def __init__(self, driver):
        self.driver = driver

    def getConfirmationText(self):
        return self.driver.find_element(*ContactUsPageLocators.CONFIRMATION_TEXT)

    def getNameInput(self):
        return self.driver.find_element(*ContactUsPageLocators.NAME_INPUT)

    def getNameError(self):
        return self.driver.find_element(*ContactUsPageLocators.NAME_ERROR)

    def getEmailInput(self):
        return self.driver.find_element(*ContactUsPageLocators.EMAIL_INPUT)

    def getEmailError(self):
        return self.driver.find_element(*ContactUsPageLocators.EMAIL_ERROR)

    def getTextInput(self):
        return self.driver.find_element(*ContactUsPageLocators.TEXT_INPUT)

    def getTextError(self):
        return self.driver.find_element(*ContactUsPageLocators.TEXT_ERROR)

    def getSubmitBtn(self):
        return self.driver.find_element(*ContactUsPageLocators.SUBMIT_BTN)

