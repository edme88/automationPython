from pytest_bdd import scenarios, given, when, then, parsers
from GerkingCourseTAU.Pages.HeaderPage import HeaderPage
from GerkingCourseTAU.Pages.SearchPage import SearchPage


CONVERTERS = {
    'product': str,
    'qty': int
}


# Scenarios
scenarios('../features/SearchResults.feature', example_converters=CONVERTERS)


# When Steps
@when(parsers.parse('search "{product}"'))
@when('search "<product>"')
def search_productName(browser, product):
    header_page = HeaderPage(browser)
    header_page.getSearchInput().send_keys(product)
    header_page.getSearchButton().click()


# Then Steps
@then(parsers.cfparse('check the quantity "{qty:Number}"  in the bottom bar', extra_types=dict(Number=int)))
@then(parsers.parse('check the quantity "{qty}"  in the bottom bar'))
@then('check the quantity "<qty>"  in the bottom bar')
def check_productQty(browser, qty):
    search_page = SearchPage(browser)

    completeText = search_page.getSearchBarBottom().text
    qtyProduct = completeText.split()[-1]
    assert int(qty) == int(qtyProduct) #if we use the parse with the type, the int(qty) is not necesary
    print('Quantity is '+str(qty))
