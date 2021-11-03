from selenium.webdriver.common.by import By


class ContributePageLocators:
    TITLE = (By.CSS_SELECTOR, 'article.item-page>h2')


class ContributePage:

    def __init__(self, driver):
        self.driver = driver

    def getTitle(self):
        return self.driver.find_element(*ContributePageLocators.TITLE)
