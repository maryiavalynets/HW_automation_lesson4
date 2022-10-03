
Feature: Test for Best Sellers page

  Scenario: BestSellers page has correct amount of links
    Given Open amazon page
    When Click on the "Best Sellers" link
    Then The BestSellers page has 5 links