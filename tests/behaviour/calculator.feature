Feature: Calculator simulator
    As a programmer 
    I want to be able to do some arithmetic operations

    Scenario: sum 3 numbers
        Given I import the interpreter
        When I type "11 + 2 + 2" and execute
        Then I should see "15"

    Scenario: subtract 2 numbers
        Given I import the interpreter
        When I type "12 - 3" and execute
        Then I should see "9"

    Scenario: divide 2 numbers
        Given I import the interpreter
        When I type "12 / 3" and execute
        Then I should see "4.0"

    Scenario: multiply 2 numbers
        Given I import the interpreter
        When I type "4 * 3" and execute
        Then I should see "12"

    Scenario: multiply 3 numbers
        Given I import the interpreter
        When I type "3 * 3 * 3" and execute
        Then I should see "27"

    Scenario: mix operations with 3 numbers with precedence
        Given I import the interpreter
        When I type "3 + 3 * 2" and execute
        Then I should see "9"

    Scenario: mix operations with 4 numbers and precedence
        Given I import the interpreter
        When I type "2 * 2 + 2 / 2" and execute
        Then I should see "5.0"
