@Contribute
Feature: When access to contribute redirect to another page
  As a user
  I want to access to contribute
  So can redirect to another page


  @ContributePage
  Scenario: Redirect to contribute page
    Given the Store webPage
    When press contribute button
    Then the title "AbanteCart Community and Contribution" is displayed in the new page
