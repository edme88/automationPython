@checkout @regression
Feature: Buy in the Store and check order ID
  As a user
  I want to buy a product in the Store
  So can check if the ID is present in the history


  @checkoutID
  Scenario: Buy in Store and check order ID
    Given the Store webPage
    When complete a buy transaction with the user "agusDarwoft" and "automation"
    Then can check if the order ID is present in the history
