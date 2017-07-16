Feature: Calculator simulator
    As a programmer 
    I want to be able to do some arithmetic operations

  Scenario: sum 2 numbers
     Given I import the interpreter
     When I type "2+3" and execute
     Then I should see "5"