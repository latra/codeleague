Feature: Join Team
  In order to join an already created team
  As a user
  I want to join a team already created

  Background: There are registered users and a team by one of them
    Given Exists a user "user1" with password "password"
    And Exists a user "user2" with password "password"
    And Exists a user "user3" with password "password"
    And Exists competition registered by "user1"
      | title        | description              | data start inscription | data finish inscription | data start competition | data finish competition |
      | Competition1 | Competition1 description | 2020-05-09             | 2020-05-20              | 2020-05-21             | 2020-05-22              |
    And Exists team at competition "Competition1" by "user2"
      | name  | members |
      | Team1 | user2   |

    Scenario: Joined an existing team
      Given I login as user "user3" with password "password"
      When I join at team "Team1"
        | name  | members      |
        | Team1 | user2, user3 |
      Then There are 2 members