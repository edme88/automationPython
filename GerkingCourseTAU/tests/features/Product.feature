@product
Feature: Download a PDF
  As a user
  I want to access to product Page
  So download the PDF

  @productOutStock
  Scenario: Check that the product is out of stock
    Given the Store webPage
    When write "BeneFit Girl Meets Pearl" and press the search button
    Then check that Out of Stock is visible
    And add to cart is not visible




