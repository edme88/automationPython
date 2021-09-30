from selenium.webdriver.common.by import By


class HeaderPageLocators:
    SEARCH_INPUT = (By.ID, 'filter_keyword')
    SEARCH_BTN = (By.CLASS_NAME, 'fa-search')
    PRODUCT_TITLE = (By.CLASS_NAME, 'bgnone')
    CHECKOUT_BTN = (By.CSS_SELECTOR, 'ul#main_menu_top li[data-id="menu_checkout"]')
    WELCOMEBACK_BTN = (By.CLASS_NAME, 'menu_text')
    LOGIN_REGISTER_BTN = (By.CSS_SELECTOR, 'ul#customer_menu_top>li>a')
    ## CART DROPDOWN
    CART_DROPDOWN = (By.CSS_SELECTOR, 'ul.topcart>li>a')
    CART_ELEMENT_1 = (By.CSS_SELECTOR, 'div#top_cart_product_list tr:nth-of-type(1) td.name')
    CART_ELEMENT_2 = (By.CSS_SELECTOR, 'div#top_cart_product_list tr:nth-of-type(2) td.name')
    CART_ELEMENT_PRICE_1 = (By.CSS_SELECTOR, 'div.products tr:nth-of-type(1) td.total')
    CART_ELEMENT_PRICE_2 = (By.CSS_SELECTOR, 'div.products tr:nth-of-type(2) td.total')
    CART_SUBTOTAL = (By.CSS_SELECTOR, 'table.totals tr:nth-of-type(1) td:nth-of-type(2)')
    CART_TOTAL = (By.CSS_SELECTOR, 'table.totals tr:nth-of-type(2) td:nth-of-type(2)')
    ## CURRENCY
    CURRENCY = (By.CSS_SELECTOR, 'ul.language>li>a')
    EURO = (By.CSS_SELECTOR, 'ul.currency li:nth-of-type(1)>a')


class HeaderPage:

    def __init__(self, driver):
        self.driver = driver

    def getSearchInput(self):
        return self.driver.find_element(*HeaderPageLocators.SEARCH_INPUT)

    def getSearchButton(self):
        return self.driver.find_element(*HeaderPageLocators.SEARCH_BTN)

    def getProductTitle(self):
        return self.driver.find_element(*HeaderPageLocators.PRODUCT_TITLE)

    def getCheckoutBtn(self):
        return self.driver.find_element(*HeaderPageLocators.CHECKOUT_BTN)

    def getWelcomeBackBtn(self):
        return self.driver.find_element(*HeaderPageLocators.WELCOMEBACK_BTN)

    def getLoginRegisterBtn(self):
        return self.driver.find_element(*HeaderPageLocators.LOGIN_REGISTER_BTN)

    ## CART DROPDOWN
    def getCartDropdown(self):
        return self.driver.find_element(*HeaderPageLocators.CART_DROPDOWN)

    def getCartElement1(self):
        return self.driver.find_element(*HeaderPageLocators.CART_ELEMENT_1)

    def getCartElement2(self):
        return self.driver.find_element(*HeaderPageLocators.CART_ELEMENT_2)

    def getCartElementPrice1(self):
        return self.driver.find_element(*HeaderPageLocators.CART_ELEMENT_PRICE_1)

    def getCartElementPrice2(self):
        return self.driver.find_element(*HeaderPageLocators.CART_ELEMENT_PRICE_2)

    def getCartSubtotal(self):
        return self.driver.find_element(*HeaderPageLocators.CART_SUBTOTAL)

    def getCartTotal(self):
        return self.driver.find_element(*HeaderPageLocators.CART_TOTAL)

    ## CURRENCY
    def getCurrency(self):
        return self.driver.find_element(*HeaderPageLocators.CURRENCY)

    def getSelectEuro(self):
        return self.driver.find_element(*HeaderPageLocators.EURO)
