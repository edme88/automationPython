@search
Feature: Search product
  As a user
  I want to write a product name
  So can see related product

  Background:
    Given the search input in the header

  @searchOK
  Scenario: Search a Product correctly
    When write "french" and press the search button
    Then See the product "New French With Ease" displayed

  @searchNOK
  Scenario: Not found a product during search
    When write "papafrita" and press enter
    Then See the text "There is no product that matches the search criteria." displayed
