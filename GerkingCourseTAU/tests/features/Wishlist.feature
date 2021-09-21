@wishlist
Feature: Add product to wishlist and check that product is present
  As a user
  I want to add product to wishlist
  So can check that product is in the list


  @checkWhislist
  Scenario: Add product to wishlist and check
    Given the Store webPage
    When the user is login with "agusDarwoft" and "automation"
    And add a "Baseball" to the wishList
    Then the "Baseball T-Shirt" is in the wishlist
