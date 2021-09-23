from selenium.webdriver.common.by import By


class FooterPageLocators():
    CONTACTUS_BTN = (By.CSS_SELECTOR, 'ul.info_links_footer li:nth-of-type(5)')

class FooterPage():

    def __init__(self, driver):
        self.driver = driver

    def getContactUs(self):
        return self.driver.find_element(*FooterPageLocators.CONTACTUS_BTN)

