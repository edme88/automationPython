@Books
Feature: When access to book sort by A-Z
  As a user
  I want to access to book page
  So can display sorted

  Background:
    Given the Store webPage
    When press book button

  Scenario: Sort books A-Z
    When select order by "Name A - Z"
    Then the books are sorted

  Scenario: Sort books Price High > Low
    When select order by "Price High > Low"
    Then the books are sorted

  Scenario: Sort books Price Low > High
    When select order by "Price Low > High"
    Then the books are sorted

