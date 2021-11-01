@menu
Feature: Check Menu in homepage
  As a user
  I want to check every option in the main menu
  So Make sure that are OK

  Background:
    Given the Store webPage

  @menuOk
  Scenario: Check options
    When get options in the menu
    Then option "1" is "HOME"
    And option "2" is "APPAREL & ACCESSORIES"
    And option "3" is "MAKEUP"
    And option "4" is "SKINCARE"
    And option "5" is "FRAGRANCE"
    And option "6" is "MEN"
    And option "7" is "HAIR CARE"
    And option "8" is "BOOKS"
