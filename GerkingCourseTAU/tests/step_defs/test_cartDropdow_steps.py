from pytest_bdd import scenarios, given, when, then, parsers
from GerkingCourseTAU.Pages.ProductPage import ProductPage
from GerkingCourseTAU.Pages.HeaderPage import HeaderPage
from selenium.webdriver.common.action_chains import ActionChains

# Scenarios
scenarios('../features/CartDropdown.feature')


# When Steps
@when(parsers.parse('add 2 products("{product1}", "{product2}") to cart'))
def add_2products_to_cart(browser, product1, product2):
    header_page = HeaderPage(browser)
    product_page = ProductPage(browser)

    header_page.getSearchInput().send_keys(product1)
    header_page.getSearchButton().click()
    product_page.getAddToCartBtn().click()
    print('First Product Added')

    header_page.getSearchInput().send_keys(product2)
    header_page.getSearchButton().click()
    product_page.getAddToCartBtn().click()
    print('Add 2 products to cart')


@when('do a mouse over the cart dropdown')
def move_over_cart_dropdown(browser):
    header_page = HeaderPage(browser)

    hover = ActionChains(browser).move_to_element(header_page.getCartDropdown())
    hover.perform()
    print('Over Cart Button')


@when('select Euro')
def select_euro(browser):
    header_page = HeaderPage(browser)

    hover = ActionChains(browser).move_to_element(header_page.getCurrency())
    hover.perform()
    header_page.getSelectEuro().click()
    print('Select Euro')


@when('select Libras')
def select_libras(browser):
    header_page = HeaderPage(browser)

    hover = ActionChains(browser).move_to_element(header_page.getCurrency())
    hover.perform()
    header_page.getSelectLibras().click()
    print('Select Libras')


# Then Steps
@then(parsers.parse('the product names are contained in the cart ("{product1}", "{product2}")'))
def text_displayed_in_cart_dropdown(browser, product1, product2):
    header_page = HeaderPage(browser)

    assert header_page.getCartElement1().text.lower() in product1.lower()
    assert header_page.getCartElement2().text.lower() in product2.lower()
    print('Product name')


@then(parsers.parse('the product prices are ("{p1}", "{p2}"), subtotal "{subtotal}" and total "{total}" in "{currency}"'))
def check_prices_in_cart_dropdown(browser, p1, p2, subtotal, total, currency):
    header_page = HeaderPage(browser)
    c1 = ""
    c2 = ""

    if currency == "€":
        c2 = currency
    else:
        c1 = currency

    assert header_page.getCartElementPrice1().text == c1 + p1 + c2
    assert header_page.getCartElementPrice2().text == c1 + p2 + c2
    assert header_page.getCartSubtotal().text == c1 + subtotal + c2
    assert header_page.getCartTotal().text == c1 + total + c2
    print('Check prices, subtotal and total')
