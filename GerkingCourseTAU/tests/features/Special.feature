@Special
Feature: Special Offers
  As a user
  I want to access to Special Offer page
  So can check each offer

  @specialOffer
  Scenario: Check special offers
    Given the Store webPage
    When press special button
    Then all the offers are displayed with the flag Sale

