@cat
Feature: Get a fact about cat
  As a user
  I want to get a fact
  So the service is working correctly

  Background:
    Given the endpoint

  @catFact
  Scenario: Get a fact about cat
    When send the max length "180"
    Then obtain a fact code "200"
