Feature: List all categories
  In order to have competitions filtered in some way
  As a user
  I want to list all the categories
  Background: There is a category and a registered user
    Given Exists a user "user" with password "password"
    And Exists a category  with password "password"
    And Exists a user "user3" with password "password"
    And Exists a competition registered by "user1"
      | title        | description              | data_start_inscription_0 | data_start_inscription_1 | data_finish_inscription_0 | data_finish_inscription_1 | data_start_competition_0 | data_start_competition_1 | data_finish_competition_0 | data_finish_competition_1 |
      | Competition1 | Competition1 description | 2020-05-09               | 17:00:00                 | 2020-05-20                | 17:00:00                  | 2020-05-21               | 17:00:00                 | 2020-05-22                | 17:00:00                  |
    And Exists team "team1" at competition "Competition1" by "user2"
    And Exists team "team2" at competition "Competition1" by "user3"

  Scenario: List all teams of a competition
    Given I login as user "user1" with password "password"
    When I list teams
    Then I'm viewing a list containing all the teams of the competition
      | name   |
      | team1  |
      | team2  |