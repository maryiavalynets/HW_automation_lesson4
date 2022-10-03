
Feature: UI test for Customer Service's page

  Scenario: Verify that UI elements are present on the page
    Given Open Customer Service page
    Then The header is present
    And  Block has 9 links
    And "Search our help library" is present
    And Input field is present
    And "All help topics" is present
    And Block of the recommended topicts has 11 links
