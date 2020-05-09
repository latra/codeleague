Feature: List all competitions
  In order to keep myself up to date about competitions registered in codeleague
  As a user
  I want to list all the competitions

  Background: There are 3 registered competitions by same user
    Given Exists a user "user" with password "password"
    And Exists competition registered by "user"
      | title        | description              | data_start_inscription_0 | data_start_inscription_1 | data_finish_inscription_0 | data_finish_inscription_1 | data_start_competition_0 | data_start_competition_1 | data_finish_competition_0 | data_finish_competition_1 |
      | Competition1 | Competition1 description | 2020-05-09               | 17:00:00                 | 2020-05-20                | 17:00:00                  | 2020-05-21               | 17:00:00                 | 2020-05-22                | 17:00:00                  |
      | Competition2 | Competition2 description | 2020-05-07               | 17:00:00                 | 2020-05-15                | 17:00:00                  | 2020-05-16               | 17:00:00                 | 2020-06-16                | 18:00:00                  |
      | Competition3 | Competition3 description | 2020-05-22               | 17:00:00                 | 2020-05-30                | 17:00:00                  | 2020-05-31               | 17:00:00                 | 2020-06-20                | 18:00:00                  |

  Scenario: List all competitions
    Given I login as user "user" with password "password"
    When I list competitions
    Then I'm viewing a list containing all the competitions
      | title        | description              | data_start_inscription_0 | data_start_inscription_1 | data_finish_inscription_0 | data_finish_inscription_1 | data_start_competition_0 | data_start_competition_1 | data_finish_competition_0 | data_finish_competition_1 |
      | Competition1 | Competition1 description | 2020-05-09               | 17:00:00                 | 2020-05-20                | 17:00:00                  | 2020-05-21               | 17:00:00                 | 2020-05-22                | 17:00:00                  |
      | Competition2 | Competition2 description | 2020-05-07               | 17:00:00                 | 2020-05-15                | 17:00:00                  | 2020-05-16               | 17:00:00                 | 2020-06-16                | 18:00:00                  |
      | Competition3 | Competition3 description | 2020-05-22               | 17:00:00                 | 2020-05-30                | 17:00:00                  | 2020-05-31               | 17:00:00                 | 2020-06-20                | 18:00:00                  |
    And The list contains 3 competitions
