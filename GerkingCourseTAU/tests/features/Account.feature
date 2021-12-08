@Account
Feature: When access to account page
  As a user
  I want to access account page
  So can check visual details

  Scenario: Check orange & grey button
    Given the Store webPage
    When complete "agusDarwoft" and "automation"
    And Login correctly
    Then all the buttons are grey by default
    And all the button are orange when hover
