@Review
Feature: Write a product review
  As a user
  I want to go to product page
  So can can write a review

  Background:
    Given the Store webPage
    When go to product page of "Benefit Bella Bamba"
    And click review tab

  @WriteReviewNoCodeVerification
  Scenario: Add a product review without verification code
    Then complete: rating "4", Name "Agustinita", Review "Este debe ser un texto de mínimo 25 caracteres"
    And press submit button
    And check text "Human verification has failed! Please try again." error

  @WriteReviewWrongCodeVerification
  Scenario: Add a product review with wrong verification code
    Then complete: rating "1", Name "Agustinita", Review "Este debe ser un texto de mínimo 25 caracteres"
    And complete verification code "00ff00"
    And press submit button
    And check text "Human verification has failed! Please try again." error

  @WriteReviewOkCodeVerification
  Scenario: Add a product review with OK verification code
    Then complete: rating "1", Name "Agustinita", Review "Este debe ser un texto de mínimo 25 caracteres"
    And complete verification code correctly
    And press submit button
    And check text "Thank you for your review. It has been submitted to the webmaster for approval."

  @WriteShortReviewOkCodeVerification
  Scenario: Add a short product review with ok verification code
    Then complete: rating "1", Name "Agustinita", Review "Short"
    And complete verification code correctly
    And press submit button
    And check text "Error: Review Text must be between 25 and 1000 characters!" error
