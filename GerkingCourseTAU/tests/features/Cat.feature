@cat
Feature: Get a fact about cat
  As a user
  I want to get a fact
  So the service is working correctly

  @catFact
  Scenario: Get a fact about cat and check response
    Given the endpoint call "/fact"
    Then obtain a fact code "200"
