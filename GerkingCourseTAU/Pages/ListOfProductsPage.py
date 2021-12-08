from selenium.webdriver.common.by import By


class ListOfProductsPageLocators:
    CONTACTUS_BTN = (By.CSS_SELECTOR, 'ul.info_links_footer li:nth-of-type(5)')
    SALE_BANNER = (By.CSS_SELECTOR, 'span.sale')
    PRODUCT_CARD = (By.CSS_SELECTOR, 'div.grid>div[class="col-md-3 col-sm-6 col-xs-12"]')


class ListOfProductsPage:

    def __init__(self, driver):
        self.driver = driver

    def getBookTitle(self, num):
        return self.driver.find_element(By.CSS_SELECTOR, 'div.grid>div:nth-of-type('+num+') a.prdocutname')

    def getSale(self):
        return self.driver.find_element(*ListOfProductsPageLocators.SALE_BANNER)

    def getSaleNum(self, num):
        return self.driver.find_element(By.CSS_SELECTOR, 'div:nth-of-type('+str(num)+') > .thumbnail > span.sale')

    def getProductCard(self):
        return self.driver.find_elements(*ListOfProductsPageLocators.PRODUCT_CARD)

    def getProductCardNum(self, num):
        return self.driver.find_element(By.CSS_SELECTOR, 'div.grid>div[class="col-md-3 col-sm-6 col-xs-12"]:nth-of-type'+str(num))
