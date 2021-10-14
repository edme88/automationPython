@searchResults
Feature: Search Results
  As a user
  I want to search a product
  So can check the quantity

  Scenario Outline: Check quantity of products
    Given the search input in the header
    When search "<product>"
    Then check the quantity "<qty>"  in the bottom bar

    Examples: Search Products
      | product | qty |
      | skin    | 3   |
      | perfume | 2   |
      | cream   | 4   |
      | spray   | 7   |

  Scenario: Check quantity of products individually
    Given the search input in the header
    When search "clean"
    Then check the quantity "3"  in the bottom bar
