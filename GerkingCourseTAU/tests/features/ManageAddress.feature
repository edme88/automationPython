@ManageAddress
Feature: In ManageAddressBook edit the direction
  As a user
  I want to edit my address
  So can check that the mew addressis displayed

  Background:
    Given the Store webPage
    When complete "agusDarwoft" and "automation"
    And press "Manage Address Book" button
    And press Edit button
    And change my adress2 for "Siempre vida 123"
    Then the message "Your address has been successfully updated" is displayed