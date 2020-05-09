Feature: Register Team
  In order to create a team
  As a user
  I want to register a team in the corresponding competition along with its name, some members and the corresponding competition

  Background: There are registered users and a competition by one of them
    Given Exists a user "user1" with password "password"
    And Exists a user "user2" with password "password"
    And Exists a user "user3" with password "password"
    And Exists a competition registered by "user1"
      | title        | description              | data start inscription | data finish inscription | data start competition | data finish competition |
      | Competition1 | Competition1 description | 2020-05-09             | 2020-05-20              | 2020-05-21             | 2020-05-22              |

  Scenario: Register a public team
    Given I login as user "user2" with password "password"
    When I register team at competition "Competition1"
      | name   | members |
      | Team 1 | user    |
    Then There are 1 teams

  Scenario: Register a team with a password
    Given I login as user "user3" with password "password"
    When I register team at competition "Competition1"
      | name   | members | password |
      | Team 2 | user    | password |
    Then There are 1 teams

  Scenario: Try to register a team but not logged in
    Given I'm not logged in
    When I want to register a team
    Then There is no "create" link available
