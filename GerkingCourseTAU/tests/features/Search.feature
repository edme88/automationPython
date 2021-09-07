@search
Feature: Search product
  As a user
  I want to write a product name
  So can see related product

  @searchOK
  Scenario: Search a Product
    Given the search input in the header
    When write "french" and press the search button
    Then See the product "French" displayed

