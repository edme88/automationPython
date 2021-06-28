import unittest
import time
from selenium.webdriver.common.by import By

class CreateAccountPage(unittest.TestCase):
    FIRST_NAME = (By.ID, 'AccountFrm_firstname')
    LAST_NAME = (By.ID, 'AccountFrm_lastname')
    EMAIL = (By.ID, 'AccountFrm_email')
    TELEPHONE = (By.ID, 'AccountFrm_telephone')
    FAX = (By.ID, 'AccountFrm_fax')
    COMPANY = (By.ID, 'AccountFrm_company')
    ADDRESS1 = (By.ID, 'AccountFrm_address_1')
    ADDRESS2 = (By.ID, 'AccountFrm_address_2')
    CITY = (By.ID, 'AccountFrm_city')
    REGION_STATE = (By.ID, 'AccountFrm_zone_id')
    ZIP_CODE = (By.ID, 'AccountFrm_postcode')
    COUNTRY = (By.ID, 'AccountFrm_country_id')
    LOGIN_NAME = (By.ID, 'AccountFrm_loginname')
    PASSWORD = (By.ID, 'AccountFrm_password')
    PASSWORD_CONFIRM = (By.ID, 'AccountFrm_confirm')
    BTN_CONTINUE = (By.CSS_SELECTOR, 'button[title="Continue"]')
    NEWSLETTER_NO = (By.ID, 'AccountFrm_newsletter0')
    POLICY = (By.ID, 'AccountFrm_agree')

    def __init__(self, driver):
        self.driver = driver

    def personalDetails(self, firstName, lastName, email, phone, fax):
        self.driver.find_element(*self.FIRST_NAME).send_keys(firstName)
        self.driver.find_element(*self.LAST_NAME).send_keys(lastName)
        self.driver.find_element(*self.EMAIL).send_keys(email)
        self.driver.find_element(*self.TELEPHONE).send_keys(phone)
        self.driver.find_element(*self.FAX).send_keys(fax)

    def addressDetails(self, company, address1, address2, city, region, zipcode, country):
        self.driver.find_element(*self.COUNTRY).send_keys(country)
        self.driver.find_element(*self.COMPANY).send_keys(company)
        self.driver.find_element(*self.ADDRESS1).send_keys(address1)
        self.driver.find_element(*self.ADDRESS2).send_keys(address2)
        self.driver.find_element(*self.CITY).send_keys(city)
        self.driver.find_element(*self.ZIP_CODE).send_keys(zipcode)
        time.sleep(2)
        self.driver.find_element(*self.REGION_STATE).send_keys(region)

    def login(self, login, password):
        self.driver.find_element(*self.LOGIN_NAME).send_keys(login)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.PASSWORD_CONFIRM).send_keys(password)
        self.driver.find_element(*self.NEWSLETTER_NO).click()
        self.driver.find_element(*self.POLICY).click()
        self.driver.find_element(*self.BTN_CONTINUE).click()