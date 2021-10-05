@Cart
Feature: Add 2 products and check dropdown cart
  As a user
  I want to add 2 products to cart
  So can see in cart dropdown

  Background:
    Given the Store webPage
    When add 2 products("Armani Code Sport", "Total Moisture Facial Cream") to cart

  @CartDropdown
  Scenario: See 2 products names in cart dropdown
    When do a mouse over the cart dropdown
    Then the product names are contained in the cart ("Armani Code Sport", "Total Moisture Facial Cream")

  @CartDropdownPrice
  Scenario: See price in Dollars of 2 products in cart dropdown
    When do a mouse over the cart dropdown
    Then the product prices are ("37.50", "38.00"), subtotal "75.50" and total "75.50" in "$"

  @CartDropdownPriceEuro
  Scenario: See price in Euros of 2 products in cart dropdown
    When select Euro
    And do a mouse over the cart dropdown
    Then the product prices are ("35.19", "35.66"), subtotal "70.85" and total "70.85" in "€"

  @CartDropdownPriceLibras
  Scenario: See price in Libras of 2 products in cart dropdown
    When select Libras
    And do a mouse over the cart dropdown
    Then the product prices are ("29.75", "30.15"), subtotal "59.90" and total "59.90" in "£"
