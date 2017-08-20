Feature: Simple code interpreter
    As a programmer
    I want to interpret some pascal code

    Scenario: interpreter runs with the empty statement
        Given I import the interpreter
        When I type "BEGIN END." and execute
        Then I should see "None"
