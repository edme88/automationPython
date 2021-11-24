from pytest_bdd import scenarios, given, when, then, parsers
from GerkingCourseTAU.Pages.FooterPage import FooterPage
from selenium.webdriver.common.action_chains import ActionChains
import time
import json
from selenium.webdriver.support.ui import WebDriverWait


# Scenarios
scenarios('../features/Testimonials.feature')


# When Steps
@when('scroll to testimonials section')
def scroll_testimonial(browser):
    footer_page = FooterPage(browser)
    testimonial_section = footer_page.getTestimonialSection()

    #actions = ActionChains(browser)
    #actions.move_to_element(testimonial_section).perform()
    browser.execute_script("arguments[0].scrollIntoView();", testimonial_section)
    print('Scroll to contribute section')


@then('check testimonial title')
def check_testimonial_title(browser):
    footer_page = FooterPage(browser)
    assert footer_page.getTestimonialTitle().text == 'TESTIMONIALS'
    print('Check testimonial title')


@then('check each testimonial and name')
def check_testimonial_user(browser):
    footer_page = FooterPage(browser)

    file = open('../../Datos/testimonials.json', "r")
    data = file.read()
    obj = json.loads(data)
    list = obj['testimonials']

    time.sleep(4)

    for i in range(len(list)):
        testimonial = list[i].get("testimonial")
        by = list[i].get("By")
        assert footer_page.getTestimonial().text == '"'+testimonial+'"'+'\n'+'By : '+by
        time.sleep(6)
        #wait = WebDriverWait(browser, 10)
        #wait.until(testimonial)
        print('Testimonial '+str(i)+' : ' + testimonial)

    print('Finish to test Testimonials')




