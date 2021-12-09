from pytest_bdd import scenarios, given, when, then, parsers
from GerkingCourseTAU.Pages.HeaderPage import HeaderPage
from selenium.webdriver.common.action_chains import ActionChains


# Scenarios
scenarios('../features/Cookie.feature')


# Whem Steps
@when('change currency for pounds')
def change_pound_currency(browser):
    header_page = HeaderPage(browser)

    hover = ActionChains(browser).move_to_element(header_page.getCurrency())
    hover.perform()
    header_page.getSelectLibras().click()
    print('Select pounds')


@when('change currency for euro')
def change_currency_euro(browser):
    header_page = HeaderPage(browser)

    hover = ActionChains(browser).move_to_element(header_page.getCurrency())
    hover.perform()
    header_page.getSelectEuro().click()
    print('Select Euro')


# Then Steps
@then(parsers.parse('verify that the "{cookie_name}" is "{cookie_value}"'))
def verify_cookie_value(browser, cookie_name, cookie_value):
    myCookie = browser.get_cookie(cookie_name)

    print('Value of the cookie '+cookie_name+' is: ')
    print(myCookie)

    assert myCookie['value'] == cookie_value
    print('Value of the cookie '+cookie_name+' is correct: '+cookie_value)
