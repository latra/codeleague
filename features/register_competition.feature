Feature: Register Competition
  In order to organize a competition
  As a user
  I want to register a competition along with its title, description, date when inscriptions start, date when
  inscriptions finish, date when competition starts, date when competitions finishes, categories, files and owner
  must be set to me

  Background: There is a registered user
    Given Exists a user "user" with password "password"

  Scenario: Register a competition without a file
    Given I login as user "user" with password "password"
    When I register a competition
      | title        | description              | data_start_inscription_0 | data_start_inscription_1 | data_finish_inscription_0 | data_finish_inscription_1 | data_start_competition_0 | data_start_competition_1 | data_finish_competition_0 | data_finish_competition_1 |
      | Competition1 | Competition1 description | 2020-05-09               | 17:00:00                 | 2020-05-20                | 17:00:00                  | 2020-05-21               | 17:00:00                 | 2020-05-22                | 17:00:00                  |
    Then I'm viewing the details page for the first competition
      | title        | description              | data start inscription | data finish inscription | data start competition | data finish competition |
      | Competition1 | Competition1 description | 2020-05-09             | 2020-05-20              | 2020-05-21             | 2020-05-22              |
    And There are 1 competitions

  Scenario: Register a competition
    Given I login as user "user" with password "password"
    When I register a competition
      | title        | description              | data_start_inscription_0 | data_start_inscription_1 | data_finish_inscription_0 | data_finish_inscription_1 | data_start_competition_0 | data_start_competition_1 | data_finish_competition_0 | data_finish_competition_1 |
      | Competition1 | Competition1 description | 2020-05-09               | 17:00:00                 | 2020-05-20                | 17:00:00                  | 2020-05-21               | 17:00:00                 | 2020-05-22                | 17:00:00                  |
    Then I'm viewing the details page for the first competition





