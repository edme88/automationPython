from selenium.webdriver.common.by import By


class AccountPageLocators():
    ORDER_HISTORY = (By.CSS_SELECTOR, 'li a[data-original-title="Order history"]')
    LAST_ORDER = (By.CSS_SELECTOR,'div.contentpanel div.mt20:nth-of-type(1)>div:nth-of-type(1)')
    WISHLIST_BTN = (By.CSS_SELECTOR, 'a[data-original-title="My wish list"]')

class AccountPage():

    def __init__(self, driver):
        self.driver = driver

    def getOrderHistoryBtn(self):
        return self.driver.find_element(*AccountPageLocators.ORDER_HISTORY)

    def getLastOrder(self):
        return self.driver.find_element(*AccountPageLocators.LAST_ORDER)

    def getWishListBtn(self):
        return self.driver.find_element(*AccountPageLocators.WISHLIST_BTN)
