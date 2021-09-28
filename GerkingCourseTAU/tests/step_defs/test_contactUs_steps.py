import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from GerkingCourseTAU.Pages.FooterPage import FooterPage
from GerkingCourseTAU.Pages.ContactUsPage import ContactUsPage

# Constants
STORE_HOME = 'https://automationteststore.com/'

# Scenarios
scenarios('../features/ContactUs.feature')

# Fixtures
@pytest.fixture
def browser():
    b = webdriver.Firefox()
    b.implicitly_wait(10)
    yield b
    b.quit()

# Given Steps
@given('the Store webPage')
def go_login_page(browser):
    browser.get(STORE_HOME)
    print('Browser is open')

# When Steps
@when('the user access to contactUs section')
def access_contactUs(browser):
    footer_page = FooterPage(browser)

    footer_page.getContactUs().click()
    print('Click Contact Us Btn')


@when(parsers.parse('complete the First name "{name}" Email "{email}" and Enquiry "{message}"'))
def complete_contact_form(browser, name, email, message):
    contact_page = ContactUsPage(browser)

    contact_page.getNameInput().send_keys(name)
    contact_page.getEmailInput().send_keys(email)
    contact_page.getTextInput().send_keys(message)
    print('Complete form')

@when('press send button')
def press_send_button(browser):
    contact_page = ContactUsPage(browser)

    contact_page.getSubmitBtn().click()
    print('Press Send')


# Then Steps
@then(parsers.parse('the text "{confirmation}" is displayed'))
def confirmation_text_displayed(browser, confirmation):
    contact_page = ContactUsPage(browser)

    assert contact_page.getConfirmationText().text == confirmation
    print('The text '+confirmation+' is displayed')


@then(parsers.parse('the text "{message}" is displayed for First name'))
def error_name(browser, message):
    contact_page = ContactUsPage(browser)

    assert contact_page.getNameError().text == message
    print('Error for First name is displayed')


@then(parsers.parse('the text "{message}" is displayed for Email'))
def error_email(browser, message):
    contact_page = ContactUsPage(browser)

    assert contact_page.getEmailError().text == message
    print('Error for Email is displayed')


@then(parsers.parse('the text "{message}" is displayed for Enquiry'))
def error_enquiry(browser, message):
    contact_page = ContactUsPage(browser)

    assert contact_page.getTextError().text == message
    print('Error for Enquiry is displayed')




