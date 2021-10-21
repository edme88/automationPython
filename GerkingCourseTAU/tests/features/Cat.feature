@catService
Feature: Get a fact about cat
  As a user
  I want to get a fact
  So the service is working correctly

  @catFactWithoutParameters
  Scenario: Get a fact about cat and check response
    Given the endpoint call "/fact"
    Then obtain a fact code "200"

  @catFactWithParameters
  Scenario: Get a fact about cat and check response
    Given the endpoint call "/fact?max_length=40"
    Then obtain a fact code "200"
