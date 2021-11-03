from selenium.webdriver.common.by import By


class FooterPageLocators:
    CONTACTUS_BTN = (By.CSS_SELECTOR, 'ul.info_links_footer li:nth-of-type(5)')
    CONTRIBUTE_BTN = (By.CSS_SELECTOR, 'div.pull-right div.b_block')


class FooterPage:

    def __init__(self, driver):
        self.driver = driver

    def getContactUs(self):
        return self.driver.find_element(*FooterPageLocators.CONTACTUS_BTN)

    def getContribute(self):
        return self.driver.find_element(*FooterPageLocators.CONTRIBUTE_BTN)

