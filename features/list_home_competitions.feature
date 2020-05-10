Feature: List competitions
  In order to keep myself up to date about competitions which will be held recently
  As a user
  I want to list the 6 competitions that are in progress and will be the next to end

  Background: There are 7 registered competitions by same user
    Given Exists a user "user" with password "password"
    And Exists competition registered by "user"
      | title        | description              | data_start_inscription_0 | data_start_inscription_1 | data_finish_inscription_0 | data_finish_inscription_1 | data_start_competition_0 | data_start_competition_1 | data_finish_competition_0 | data_finish_competition_1 |
      | Competition1 | Competition1 description | 2020-05-09               | 17:00:00                 | 2020-05-20                | 17:00:00                  | 2020-05-21               | 17:00:00                 | 2020-05-22                | 17:00:00                  |
      | Competition2 | Competition2 description | 2020-05-07               | 17:00:00                 | 2020-05-15                | 17:00:00                  | 2020-05-16               | 17:00:00                 | 2020-06-16                | 18:00:00                  |
      | Competition3 | Competition3 description | 2020-05-22               | 17:00:00                 | 2020-05-30                | 17:00:00                  | 2020-05-31               | 17:00:00                 | 2020-06-20                | 18:00:00                  |
      | Competition4 | Competition4 description | 2020-05-23               | 17:00:00                 | 2020-05-27                | 17:00:00                  | 2020-05-28               | 17:00:00                 | 2020-05-29                | 17:00:00                  |
      | Competition5 | Competition5 description | 2020-05-26               | 17:00:00                 | 2020-05-30                | 17:00:00                  | 2020-05-31               | 17:00:00                 | 2020-06-01                | 18:00:00                  |
      | Competition6 | Competition6 description | 2020-06-02               | 17:00:00                 | 2020-06-05                | 17:00:00                  | 2020-06-06               | 17:00:00                 | 2020-06-06                | 18:00:00                  |
      | Competition7 | Competition7 description | 2020-06-12               | 17:00:00                 | 2020-06-20                | 17:00:00                  | 2020-06-21               | 17:00:00                 | 2020-06-24                | 18:00:00                  |


  Scenario: List 6 competitions that will be the most recent to end
    Given I login as user "user" with password "password"
    When I am at "league:home" page
    Then I'm viewing a list containing 6 competitions
      | title        | description              | data_start_inscription_0 | data_start_inscription_1 | data_finish_inscription_0 | data_finish_inscription_1 | data_start_competition_0 | data_start_competition_1 | data_finish_competition_0 | data_finish_competition_1 |
      | Competition1 | Competition1 description | 2020-05-09               | 17:00:00                 | 2020-05-20                | 17:00:00                  | 2020-05-21               | 17:00:00                 | 2020-05-22                | 17:00:00                  |
      | Competition2 | Competition2 description | 2020-05-07               | 17:00:00                 | 2020-05-15                | 17:00:00                  | 2020-05-16               | 17:00:00                 | 2020-06-16                | 18:00:00                  |
      | Competition3 | Competition3 description | 2020-05-22               | 17:00:00                 | 2020-05-30                | 17:00:00                  | 2020-05-31               | 17:00:00                 | 2020-06-20                | 18:00:00                  |
      | Competition4 | Competition4 description | 2020-05-23               | 17:00:00                 | 2020-05-27                | 17:00:00                  | 2020-05-28               | 17:00:00                 | 2020-05-29                | 17:00:00                  |
      | Competition5 | Competition5 description | 2020-05-26               | 17:00:00                 | 2020-05-30                | 17:00:00                  | 2020-05-31               | 17:00:00                 | 2020-06-01                | 18:00:00                  |
      | Competition6 | Competition6 description | 2020-06-02               | 17:00:00                 | 2020-06-05                | 17:00:00                  | 2020-06-06               | 17:00:00                 | 2020-06-06                | 18:00:00                  |
    And The list contains 6 competitions
      | title        |
      | Competition1 |
      | Competition2 |
      | Competition3 |
      | Competition4 |
      | Competition5 |
      | Competition6 |

  Scenario: Try to list 6 most recent to end competitions but not logged in
    Given I'm not logged in
    When I am at "league:home" page
    Then There is no competitions at page
      | title        |
      | Competition1 |
      | Competition2 |
      | Competition3 |
      | Competition4 |
      | Competition5 |
      | Competition6 |
