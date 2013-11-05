Feature: Base Theme
    As a developer
    I want to have base theme for Phoenix
    So that I can make child theme

    Scenario: Check HTML structure on base theme
        Given I visit "http://mymelody.dev.bypronto.com"
        Then I should see content on base theme
