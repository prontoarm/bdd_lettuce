Feature: User searches on Amazon

  Background:
    Given I visit "http://www.amazon.com"

  Scenario: User performs search
    When I fill in "field-keywords" with "xbox"
    And I press "Go"
    Then I should see "Results"

  Scenario: User performs search
    When I fill in "field-keywords" with "cover"
    And I press "Go"
    Then I should see "Results"
