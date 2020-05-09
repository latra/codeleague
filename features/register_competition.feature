Feature: Register Competition
  In order to organize a competition
  As a user
  I want to register a competition along with its title, description, date when inscriptions start, date when
  inscriptions finish, date when competition starts, date when competitions finishes, categories, files and owner
  must be set to me

  Background: There is a registered user
    Given Exists a user "user" with password "password"

  Scenario: Register a competition without a file
    Given I login as a user "user" with password "password"
    When I register a competition
      | title        | description              | data start inscription | data finish inscription | data start competition | data finish competition |
      | Competition1 | Competition1 description | 2020-05-09             | 2020-05-20              | 2020-05-21             | 2020-05-22              |
    Then I'm viewing the home page where there are the details of all the competitions created
      | title        | description              | data start inscription | data finish inscription | data start competition | data finish competition |
      | Competition1 | Competition1 description | 2020-05-09             | 2020-05-20              | 2020-05-21             | 2020-05-22              |
    And There are 1 competitions

  Scenario: Register a competition
    Given I login as a user "user" with password "password"
    When I register a competition
      | title         | description              | data start inscription | data finish inscription | data start competition | data finish competition | files              |
      | Competition1  | Competition1 description | 2020-05-09             | 2020-05-20              | 2020-05-21             | 2020-05-22              | features/comp1.jpg |
    Then I'm vewing the home page where there are the details of all the competitions created





