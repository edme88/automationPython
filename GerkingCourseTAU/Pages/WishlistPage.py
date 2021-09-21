from selenium.webdriver.common.by import By


class WishlistPageLocators():
    TABLE_WISH = (By.CSS_SELECTOR, 'div.product-list table tr td.align_left:nth-of-type(2) a')

class WishlistPage():

    def __init__(self, driver):
        self.driver = driver

    def getTableWish(self):
        return self.driver.find_element(*WishlistPageLocators.TABLE_WISH)

