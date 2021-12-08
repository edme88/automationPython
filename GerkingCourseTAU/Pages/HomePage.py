from selenium.webdriver.common.by import By


class HomePageLocators:
    BANNER = (By.CLASS_NAME, 'oneByOneSlide')
    BANNER_IMG = (By.CSS_SELECTOR, 'p[style="display: block;"] img')


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def getBanner(self):
        return self.driver.find_element(*HomePageLocators.BANNER)

    def getBannerImage(self):
        return self.driver.find_element(*HomePageLocators.BANNER_IMG)
