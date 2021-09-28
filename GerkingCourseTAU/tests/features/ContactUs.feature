@ContactUS
Feature: In contactUs section send a message and check the confirmation
  As a user
  I want to send a message
  So can check that the confirmation is displayed

  Background:
    Given the Store webPage
    When the user access to contactUs section

  @sendContactUsMessage
  Scenario: Send a contactUs message and check text
    When complete the First name "Agustinita" Email "agustina.aliciardi@darwoft.com" and Enquiry "Hello testers!"
    And press send button
    Then the text "Your enquiry has been successfully sent to the store owner!" is displayed

  @CheckFormErrors
  Scenario: Send contactUs form empty
    When press send button
    Then the text "First name: is required field! Name must be between 3 and 32 characters!" is displayed for First name
    And the text "Email: is required field! E-Mail Address does not appear to be valid!" is displayed for Email
    And the text "Enquiry: is required field! Enquiry must be between 10 and 3000 characters!" is displayed for Enquiry


