Feature: Compute factorials
    As an example
    So that I can demonstrate lettuce
    I want to calculate factorials of numbers

    Scenario Outline: Factorial of various numbersers
        Given I have an input of <input>
        When I calculate its Factorial
        Then I should get a result of <result>

        Examples:
            | input | result    |
            | 1     | 1         |
            | 2     | 2         |
            | 3     | 6         |
            | 4     | 24        |
            | 5     | 120       |
            | 6     | 720       |

