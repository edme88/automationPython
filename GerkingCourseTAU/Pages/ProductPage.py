from selenium.webdriver.common.by import By
import urllib.request
from PIL import Image
import os
import pytesseract


class ProductPageLocators:
    ADD_TO_CART = (By.CSS_SELECTOR, 'div.jumbotron a[data-id="74"]')
    ADD_TO_WISHLIST = (By.CLASS_NAME, 'wishlist_add')
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, 'ul.productpagecart a')
    PRINT_BTN = (By.CLASS_NAME, 'productprint')
    SAVE_BTN = (By.CSS_SELECTOR, 'cr-button.action-button')
    OUT_STOCK = (By.CLASS_NAME, 'nostock')
    ## REVIEW
    REVIEW_TAB = (By.CSS_SELECTOR, 'ul#myTab li:nth-of-type(2)')
    NAME_INPUT = (By.ID, 'name')
    REVIEW_TEXT = (By.ID, 'text')
    CAPCHA_IMG = (By.ID, 'captcha_img')
    CAPTCHA_INPUT = (By.ID, 'captcha')
    SUBMIT_BTN = (By.ID, 'review_submit')
    ERROR_MSG = (By.CLASS_NAME, 'alert-error')
    OK_MSG = (By.CLASS_NAME, 'alert-success')

class ProductPage:

    def __init__(self, driver):
        self.driver = driver

    def getAddToCard(self):
        return self.driver.find_element(*ProductPageLocators.ADD_TO_CART)

    def getAddToWishlist(self):
        return self.driver.find_element(*ProductPageLocators.ADD_TO_WISHLIST)

    def getAddToCartBtn(self):
        return self.driver.find_element(*ProductPageLocators.ADD_TO_CART_BTN)

    def getPrintBtn(self):
        return self.driver.find_element(*ProductPageLocators.PRINT_BTN)

    def getSaveBtn(self):
        return self.driver.find_element(*ProductPageLocators.SAVE_BTN)

    def getOutStock(self):
        return self.driver.find_element(*ProductPageLocators.OUT_STOCK)

    ## REVIEW
    def getReviewTab(self):
        return self.driver.find_element(*ProductPageLocators.REVIEW_TAB)

    def getRatingStar(self, number):
        return self.driver.find_element(By.ID, 'rating'+number)

    def getReviewText(self):
        return self.driver.find_element(*ProductPageLocators.REVIEW_TEXT)

    def getReviewName(self):
        return self.driver.find_element(*ProductPageLocators.NAME_INPUT)

    def getReviewImage(self):
        path = self.driver.find_element(By.ID, 'captcha_img').get_attribute('src')
        urllib.request.urlretrieve(path, "..\..\..\OCR\indexNUEVASO.jpg")
        print(path+" image saved")
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        text = pytesseract.image_to_string(Image.open(os.path.abspath('..\..\..\OCR\indexNUEVASO.jpg')))
        print(text)
        return text

    def getReviewCaptcha(self):
        return self.driver.find_element(*ProductPageLocators.CAPTCHA_INPUT)

    def getSubmitButton(self):
        return self.driver.find_element(*ProductPageLocators.SUBMIT_BTN)

    def getErrorMsg(self):
        return self.driver.find_element(*ProductPageLocators.ERROR_MSG)

    def getOkMsg(self):
        return self.driver.find_element(*ProductPageLocators.OK_MSG)
