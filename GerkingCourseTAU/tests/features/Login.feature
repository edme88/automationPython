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

  @forgotLoginError
  Scenario: Error when try to get account with wrong data
    When press Forgot login option
    And complete with lastname "agus" and email "agus"
    Then Error "Error: No records found matching information your provided, please check your information and try again!" is displayed

  @forgotLoginOk
  Scenario: Message OK when try to get account
    When press Forgot login option
    And complete with lastname "alici" and email "agustina.aliciardi@darwoft.com"
    Then Message "Success: Your login name reminder has been sent to your e-mail address." is displayed