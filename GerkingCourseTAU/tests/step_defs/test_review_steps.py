import pytest
import pytesseract
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from GerkingCourseTAU.Pages.ProductPage import ProductPage
from GerkingCourseTAU.Pages.HeaderPage import HeaderPage


# Constants
STORE_HOME = 'https://automationteststore.com/'

# Scenarios
scenarios('../features/Review.feature')

# Fixtures
@pytest.fixture
def browser():
    b = webdriver.Firefox()
    b.implicitly_wait(10)
    yield b
    b.quit()


# When Steps
@when(parsers.parse('go to product page of "{product}"'))
def see_product_page(browser, product):
    header_page = HeaderPage(browser)

    header_page.getSearchInput().send_keys(product)
    header_page.getSearchButton().click()
    print('Product Page: '+product)


@when('click review tab')
def click_review_tab(browser):
    product_page = ProductPage(browser)

    product_page.getReviewTab().click()
    print('Click review button')


# Then Steps
@then(parsers.parse('complete: rating "{num_rating}", Name "{name}", Review "{comment}"'))
def complete_review(browser, num_rating, name, comment):
    product_page = ProductPage(browser)

    product_page.getRatingStar(num_rating).click()
    product_page.getReviewName().send_keys(name)
    product_page.getReviewText().send_keys(comment)
    print('Complete: Rating, Name, Comment')


@then('press submit button')
def press_submit_button(browser):
    product_page = ProductPage(browser)

    product_page.getSubmitButton().click()
    print('Press Submit Button')

@then('complete verification code correctly')
def complete_verification_code_ok(browser):
    product_page = ProductPage(browser)

    newkey = product_page.getReviewImage()
    product_page.getReviewCaptcha().send_keys(newkey)
    print('Complete OK verification code')


@then(parsers.parse('check text "{message}" error'))
def check_error_message(browser, message):
    product_page = ProductPage(browser)

    assert message in product_page.getErrorMsg().text
    print('Check "'+message+'" message')

@then(parsers.parse('check text "{message}"'))
def check_message(browser, message):
    product_page = ProductPage(browser)

    assert message in product_page.getOkMsg().text
    print('Check "'+message+'" message')


@then(parsers.parse('complete verification code "{verificationCode}"'))
def complete_verification_code(browser, verificationCode):
    product_page = ProductPage(browser)

    product_page.getReviewCaptcha().send_keys(verificationCode)
    print('Complete wrong verification code')

    #pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Admin\Desktop\automationPython\OCR\tesseract-ocr-w64-setup-v5.0.0-alpha.20210811'
    #text = pytesseract.image_to_string(r'C:\Users\Admin\Desktop\automationPython\OCR\index.jpg')
    #print(text)