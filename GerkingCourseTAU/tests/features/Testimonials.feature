@Testimonials
Feature: When see the testimonials check each one
  As a user
  I want to see all the testimonials
  So can check the text


  @Testimonial
  Scenario: Check testimonials
    Given the Store webPage
    When scroll to testimonials section
    Then check testimonial title
    And check each testimonial and name
