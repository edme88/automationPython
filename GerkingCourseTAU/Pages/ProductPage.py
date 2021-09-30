from selenium.webdriver.common.by import By


class ProductPageLocators:
    ADD_TO_CART = (By.CSS_SELECTOR, 'div.jumbotron a[data-id="74"]')
    ADD_TO_WISHLIST = (By.CLASS_NAME, 'wishlist_add')
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, 'ul.productpagecart a')


class ProductPage:

    def __init__(self, driver):
        self.driver = driver

    def getAddToCard(self):
        return self.driver.find_element(*ProductPageLocators.ADD_TO_CART)

    def getAddToWishlist(self):
        return self.driver.find_element(*ProductPageLocators.ADD_TO_WISHLIST)

    def getAddToCartBtn(self):
        return self.driver.find_element(*ProductPageLocators.ADD_TO_CART_BTN)
