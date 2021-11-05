# automationPython
Automation test with Python and Selenium

### How to start?
Remember to download chromedriver.exe to a 'Drivers' folder in the root.

Run the command 
* pip install
* pip install pytest-bdd
* pip install html-testRunner
* pip install pytest-html-reporter
* pip install pytest-html
* pip install -U pytest
* pip install pytesseract
* python -m pip install requests

Pluing recomended: [Ranorex Selocity](https://chrome.google.com/webstore/detail/ranorex-selocity/ocgghcnnjekfpbmafindjmijdpopafoe)

### To generate a new file with requirements
pip freeze > requirements.txt

### Pages to Practice
- POMDemo: Tets for http://automationpractice.com/
- Store: Test for https://automationteststore.com/
  
### Generate Reports
> cd Store
> cd Tests
> pytest LoginTest.py RegisterTest.py

### Run with TAGs
python -m pytest -k "searchResults"

## Courses
* TAU: [Behavior-Driven Python with pytest-bdd](https://testautomationu.applitools.com/behavior-driven-python-with-pytest-bdd/))
* Udemy: [Learn Selenium Python from scratch with Sample Projects](https://naranja.udemy.com/course/selenium-python-step-by-step-for-beginners/learn/lecture/23643210#overview)
* Darwoft

## Documentation to Read
* https://recursospython.com/guias-y-manuales/colorama-texto-fondo-coloreados-la-consola/

### Course: TAU
Scenarios:
* Cart Dropdown
  * See 2 products names in cart dropdown
  * See price in Dollars of 2 products in cart dropdown
  * See price in Euros of 2 products in cart dropdown
  * See price in Libras of 2 products in cart dropdown
* Cat
  * Get a fact about cat and check response
* Checkout
  * Buy in the Store and check order ID
* ContactUs
  * Send a contactUs message and check text
* Login
  * Login in Store Page correctly
  * Error in Login
* Review
  * Add a product review without verification code
  * Add a product review with wrong verification code
  * Add a product review with OK verification code
  * Add a short product review with ok verification code
* Search
  * Search a Product correctly
  * Not found a product during search
* SearchResults
  * Check quantity of products
* Wishlist
  * Add product to wishlist and check

### Course: Darwoft
Scenarios:
* Login
  * test_invalid_login_noUser_noPass 
  * test_login(self)
* Register
  * test_registration_fields_incomplete
  * test_registration_fail_alredy_register
  * test_registration_checkLongText
* Checkout
  * checkout_flow_with_product

### Course: Udemy
Scenarios:
* Login
  * test_invalid_username_password
  * test_invalid_without_username_password
  * test_invalid_without_password
  * test_valid_login
  * test_try_create_account

## TAREA
* Listo (/)

## Run a test and generate report
python -m pytest -k "Contribute"
pytest -m -b
python -m pytest --html=Reportes/EjemploReporte.html
python -m pytest -k test_contribute_steps
python -m pytest -k test_contribute_steps --html=EjemploReporte.html
--self --container

## Run all the test and generate reports
python -m pytest


----
## Otros Escenarios
* Presionar la lupa, buscar por categoría, checkbox
* Home ->Loguearse -> Manage Address Book -> Edit -> Cambiar dirección -> Verificar mensaje verde y nueva dirección
* Presionar contribute y en nueva página ver el título


----
Move to Element
https://stackoverflow.com/questions/34562095/scrollintoview-vs-movetoelement
https://stackoverflow.com/questions/41744368/scrolling-to-element-using-webdriver

