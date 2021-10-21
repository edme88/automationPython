import requests
from pytest_bdd import scenarios, given, then, parsers
from colorama import Fore, Back, Style

# Constants
CAT_API = 'https://catfact.ninja/'

# Scenarios
scenarios('../features/Cat.feature')

# Given Steps
@given(parsers.parse('the endpoint call "{urlEndpoint}"'), target_fixture='do_get')
def do_get(urlEndpoint):
    params = {'format': 'json'}
    response = requests.get(CAT_API + urlEndpoint)
    print(Fore.GREEN+'Complete Response: '+response.text)
    print(response.text)
    json_response = response.json()
    oneFact = json_response['fact']
    print(Back.BLUE+Fore.BLACK+Style.BRIGHT+'Print only the fact: '+oneFact)
    return response

# Then Steps
@then(parsers.parse('obtain a fact code "{code:d}"'))
def verify(do_get, code):
    assert do_get.status_code == code
    print(Back.RESET+Fore.RESET+Style.DIM+'Successful response')
