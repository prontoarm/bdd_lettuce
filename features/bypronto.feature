Feature: User searches on Amazon

  #Background:
  # Given I visit "http://dev.bypronto.com/wp-admin"

  Scenario: User performs search
    Given I visit "http://dev.bypronto.com/wp-admin"
    When I fill in "user_login" with "armeo11"
      And I fill in "user_password" with "M@rwin11"
      And I press "Log In"
    Then I should see "Results"
