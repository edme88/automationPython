import requests
from pytest_bdd import scenarios, given, when, then, parsers

# Constants
CAT_API = 'https://catfact.ninja/'

# Scenarios
scenarios('../features/Cat.feature')

# Fixtures
@pytest.fixture
def browser():
    b = webdriver.Firefox()
    b.implicitly_wait(10)
    yield b
    b.quit()

# Given Steps
@given('the endpoint')
def do_get_no_params(browser):
    browser.get(CAT_API)

@when('send the max length "180"')
def do_get(browser, len):
    params = {'len': len, 'format': 'json'}
    response = requests.get(CAT_API, params)
    return response

@then(parsers.parse('obtain a fact code "{code:d}"'))
def verify(do_get, code):
    assert do_get.status_code == code