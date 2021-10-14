from selenium.webdriver.common.by import By


class SearchPageLocators():
    SEARCH_TITLE = (By.CLASS_NAME, 'maintext')
    SEARCH_SUBTITLE = (By.CSS_SELECTOR, 'div.form-inline+h4.heading4')
    SEARCH_TEXT = (By.CSS_SELECTOR, 'div.form-inline+h4.heading4+div')
    SEARCH_BAR_BOTTOM = (By.CSS_SELECTOR, 'form[class="form-inline pull-left"]')

class SearchPage():

    def __init__(self, driver):
        self.driver = driver

    def getSearchTitle(self):
        return self.driver.find_element(*SearchPageLocators.SEARCH_TITLE)

    def getSearchSubtitle(self):
        return self.driver.find_element(*SearchPageLocators.SEARCH_SUBTITLE)

    def getSearchText(self):
        return self.driver.find_element(*SearchPageLocators.SEARCH_TEXT)

    def getSearchBarBottom(self):
        return self.driver.find_element(*SearchPageLocators.SEARCH_BAR_BOTTOM)
