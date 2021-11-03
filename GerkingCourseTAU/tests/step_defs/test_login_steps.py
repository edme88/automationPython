from pytest_bdd import scenarios, given, when, then, parsers

# Scenarios
scenarios('../features/Login.feature')


@when(parsers.parse('complete "{user}" and "{password}"'))
def complete_user_pass(browser, user, password):
    browser.find_element_by_css_selector('#customer_menu_top > li').click()
    browser.implicitly_wait(100)
    browser.find_element_by_id('loginFrm_loginname').send_keys(user)
    browser.find_element_by_id('loginFrm_password').send_keys(password)
    browser.find_element_by_css_selector('button[title="Login"]').click()


@then("Login correctly")
def check_title(browser):
    assert browser.find_element_by_css_selector('h1 span.maintext').text == 'MY ACCOUNT'


@then("Error in Login")
def check_error_title(browser):
    assert 'Error: Incorrect login or password provided.' in browser.find_element_by_css_selector('div.alert-error').text

#http://thetestingworldapi.com/Help
#https://reqres.in/