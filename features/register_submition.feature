Feature: Register submission
  In order to publish the answer of the problem raised in the competition
  As a user
  I want upload the solution for the competition

  Background: There is a team registered in a competition and some users
    Given Exists a user "user1" password "password"
    And Exists a user "user2" password "password"
    And Exists competition registered by "user1"
      | title        | description              | data_start_inscription_0 | data_start_inscription_1 | data_finish_inscription_0 | data_finish_inscription_1 | data_start_competition_0 | data_start_competition_1 | data_finish_competition_0 | data_finish_competition_1 |
      | Competition1 | Competition1 description | 2020-05-09               | 17:00:00                 | 2020-05-20                | 17:00:00                  | 2020-05-21               | 17:00:00                 | 2020-05-22                | 17:00:00                  |
    And Exists a team "team1" at competition "Competition1" by "user2"

  Scenario: Register submission
    Given I login as user "user2" with password "password"
    When I register a submission
    Then I'm at "competition/id/1/submit-answer/"
    ...
    Then
    And there are 1 submissions

  Scenario: Try to register submissions but not logged in
    Given I'm not logged in
    When I want to create a submission for a competition
    Then Need to login to have "competition/id/1/submit-answer/" link available