@log
Feature: Login in Store
  As a user
  I want to access the Store page
  So Login correctly

  Background:
    Given the Store webPage

  @logg
  Scenario: Login in Store Page correctly
    When complete user and pass
    Then Login correctly


