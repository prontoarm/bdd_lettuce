Feature: Compute factorials
    As an example
    So that I can demonstrate lettuce
    I want to calculate factorials of numbers

    Scenario: Factorial of 0
        Given I have an input of 0
        When I calculate its factorial
        Then I see the number 1

    Scenario: Factorial of 1
        Given I have an input of 1
        When I calculate its factorial
        Then I see the number 1

    Scenario: Factorial of 2
        Given I have an input of 2
        When I calculate its factorial
        Then I see the number 2

    Scenario: Factorial of 3
        Given I have an input of 3
        When I calculate its factorial
        Then I see the number 6

    Scenario: Factorial of 4
        Given I have an input of 4
        When I calculate its factorial
        Then I see the number 24
