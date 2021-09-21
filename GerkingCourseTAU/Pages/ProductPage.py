from selenium.webdriver.common.by import By


class ProductPageLocators():
    ADD_TO_CART = (By.CSS_SELECTOR, 'div.jumbotron a[data-id="74"]')
    ADD_TO_WISHLIST = (By.CLASS_NAME, 'wishlist_add')

class ProductPage():

    def __init__(self, driver):
        self.driver = driver

    def getAddToCard(self):
        return self.driver.find_element(*ProductPageLocators.ADD_TO_CART)

    def getAddToWishlist(self):
        return self.driver.find_element(*ProductPageLocators.ADD_TO_WISHLIST)
