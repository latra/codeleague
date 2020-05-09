Feature: Join Team
  In order to join an already created team
  As a user
  I want to join a team already created

  Background: There are registered users and a team by one of them
    Given Exists a user "user1" with password "password"
    And Exists a user "user2" with password "password"
    And Exists a user "user3" with password "password"
    And Exists competition registered by "user1"
      | title        | description              | data_start_inscription_0 | data_start_inscription_1 | data_finish_inscription_0 | data_finish_inscription_1 | data_start_competition_0 | data_start_competition_1 | data_finish_competition_0 | data_finish_competition_1 |
      | Competition1 | Competition1 description | 2020-05-09               | 17:00:00                 | 2020-05-20                | 17:00:00                  | 2020-05-21               | 17:00:00                 | 2020-05-22                | 17:00:00                  |
    And Exists team "team1" at competition "Competition1" by "user2"

    Scenario: Joined an existing team
      Given I login as user "user3" with password "password"
      When I join at team "Team1"
      Then There are 2 members