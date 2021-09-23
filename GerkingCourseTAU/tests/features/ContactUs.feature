@ContactUS
Feature: In contactUs section send a message and check the confirmation
  As a user
  I want to send a message
  So can check that the confirmation is displayed


  @sendContactUsMessage
  Scenario: Send a contactUs message and check text
    Given the Store webPage
    When the user access to contactUs section
    And complete the First name "Agustinita" Email "agustina.aliciardi@darwoft.com" and Enquiry "Hello testers!"
    Then the text "Your enquiry has been successfully sent to the store owner!" is displayed
