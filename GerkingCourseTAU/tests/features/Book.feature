@Books
Feature: When access to book sort by A-Z
  As a user
  I want to access to book page
  So can display sorted


  @Regression
  Scenario: Sort books A-Z
    Given the Store webPage
    When press book button
    And select order by "Name A - Z"
    Then the books are sorted

