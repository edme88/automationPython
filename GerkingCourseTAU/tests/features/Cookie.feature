@cookies
Feature: Check cookies
  As a user
  I want to see cookies
  So can check the value

  Background:
    Given the Store webPage

  @currencyCookie
  Scenario: Get the value of a cookie
    Then verify that the "currency" is "USD"

  @currencyCookiePound
  Scenario: Get the value of a cookie when change currency for Pounds
    When change currency for pounds
    Then verify that the "currency" is "GBP"

  @currencyCookieEuro
  Scenario: Get the value of a cookie when change currency for Euro
    When change currency for euro
    Then verify that the "currency" is "EUR"
