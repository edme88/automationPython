from selenium.webdriver.common.by import By


class ContactUsPageLocators():
    CONFIRMATION_TEXT = (By.CSS_SELECTOR, 'section.mb40 p:nth-of-type(2)')
    NAME_INPUT = (By.ID, 'ContactUsFrm_first_name')
    EMAIL_INPUT = (By.ID, 'ContactUsFrm_email')
    TEXT_INPUT = (By.ID, 'ContactUsFrm_enquiry')
    SUBMIT_BTN = (By.CSS_SELECTOR, 'button[title="Submit"]')

class ContactUsPage():

    def __init__(self, driver):
        self.driver = driver

    def getConfirmationText(self):
        return self.driver.find_element(*ContactUsPageLocators.CONFIRMATION_TEXT)

    def getNameInput(self):
        return self.driver.find_element(*ContactUsPageLocators.NAME_INPUT)

    def getEmailInput(self):
        return self.driver.find_element(*ContactUsPageLocators.EMAIL_INPUT)

    def getTextInput(self):
        return self.driver.find_element(*ContactUsPageLocators.TEXT_INPUT)

    def getSubmitBtn(self):
        return self.driver.find_element(*ContactUsPageLocators.SUBMIT_BTN)

