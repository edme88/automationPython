@login
Feature: Login in Store
  As a user
  I want to access the Store page
  So Login correctly

  Background:
    Given the Store webPage

  @loginOK
  Scenario: Login in Store Page correctly
    When complete "agusDarwoft" and "automation"
    Then Login correctly

  @loginwrong
  Scenario: Error in Login
    When complete "myUsu@email.com" and "papafrita"
    Then Error in Login

