from pytest_bdd import scenarios, given, when, then, parsers
from GerkingCourseTAU.Pages.HeaderPage import HeaderPage
from GerkingCourseTAU.Pages.ListOfProductsPage import ListOfProductsPage
import json


# Scenarios
scenarios('../features/Book.feature')


# When Steps
@when('press book button')
def press_book_button(browser):
    header_page = HeaderPage(browser)

    header_page.getBookOption().click()
    print('Click BOOK button')


@when(parsers.parse('select order by "{category}"'), target_fixture='order_by')
def order_by(browser, category):
    header_page = HeaderPage(browser)
    # Scroll to selector
    browser.execute_script("arguments[0].scrollIntoView();", header_page.getSortDropdown())
    header_page.getSortDropdown().click()
    header_page.selectSortOption(category).click()
    print('Select '+category)
    return category


@then(parsers.parse('the books are sorted'))
def book_sorted(browser, order_by):
    list_product_page = ListOfProductsPage(browser)

    file = open('../../Datos/books.json', "r")
    data = file.read()
    obj = json.loads(data)
    list = obj['books']
    print('Unordered list: ')
    print(list)

    if order_by == "Price High > Low" or order_by == 'Price Low > High':
        list.sort(key=lambda x: x["price"])
        print('Sort by price list: ')
        print(list)

        if order_by == "Price High > Low":
            list.reverse()
            print('Reverse Price list: ')
            print(list)


    for i in range(len(list)):
        title = list[i].get("title")
        assert list_product_page.getBookTitle(str(i+1)).text == title.upper()
        print('Title ' + str(i+1) + ' : ' + title)

    print('All the titles are checked')
