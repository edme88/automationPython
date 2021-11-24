from selenium.webdriver.common.by import By


class ListOfProductsPageLocators:
    CONTACTUS_BTN = (By.CSS_SELECTOR, 'ul.info_links_footer li:nth-of-type(5)')


class ListOfProductsPage:

    def __init__(self, driver):
        self.driver = driver

    def getBookTitle(self, num):
        return self.driver.find_element(By.CSS_SELECTOR, 'div.grid>div:nth-of-type('+num+') a.prdocutname')
