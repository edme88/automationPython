from selenium.webdriver.common.by import By


class FooterPageLocators:
    CONTACTUS_BTN = (By.CSS_SELECTOR, 'ul.info_links_footer li:nth-of-type(5)')
    CONTRIBUTE_BTN = (By.CSS_SELECTOR, 'div.pull-right div.b_block')
    TESTIMONIAL_SECTION = (By.CSS_SELECTOR, 'div[class="col-md-3"]:nth-of-type(3)')
    TESTIMONIAL_TITLE = (By.CSS_SELECTOR, '#block_frame_html_block_1777 h2')
    TESTIMONIAL = (By.CSS_SELECTOR, 'li[class="flex-active-slide"]')

class FooterPage:

    def __init__(self, driver):
        self.driver = driver

    def getContactUs(self):
        return self.driver.find_element(*FooterPageLocators.CONTACTUS_BTN)

    def getContribute(self):
        return self.driver.find_element(*FooterPageLocators.CONTRIBUTE_BTN)

    def getTestimonialSection(self):
        return self.driver.find_element(*FooterPageLocators.TESTIMONIAL_SECTION)

    def getTestimonialTitle(self):
        return self.driver.find_element(*FooterPageLocators.TESTIMONIAL_TITLE)

    def getTestimonial(self):
        return self.driver.find_element(*FooterPageLocators.TESTIMONIAL)

