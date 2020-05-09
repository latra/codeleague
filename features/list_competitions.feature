Feature: List all competitions
  In order to keep myself up to date about competitions registered in codeleague
  As a user
  I want to list all the competitions

  Background: There are 3 registered competitions by same user
    Given Exists a user "user" with password "password"
    And I login as user "user" with password "password"
    And Exists competition registered by "user"
      | title         | description              | data start inscription | data finish inscription | data start competition | data finish competition | files     |
      | Competition1  | Competition1 description | 2020-05-09             | 2020-05-20              | 2020-05-21             | 2020-05-22              | comp1.jpg |
      | Competition2  | Competition2 description | 2020-05-07             | 2020-05-15              | 2020-05-16             | 2020-05-16              | comp2.jpg |
      | Competition3  | Competition3 description | 2020-05-22             | 2020-05-30              | 2020-05-31             | 2020-05-31              | comp3.jpg |

  Scenario: List them all
    Given I login as user "user" with password "password"
    When I list competitions
    Then I'm viewing a list containing all the competitions
      | title         | description              | data start inscription | data finish inscription | data start competition | data finish competition |
      | Competition1  | Competition1 description | 2020-05-09             | 2020-05-20              | 2020-05-21             | 2020-05-22              |
      | Competition2  | Competition2 description | 2020-05-07             | 2020-05-15              | 2020-05-16             | 2020-05-16              |
      | Competition3  | Competition3 description | 2020-05-22             | 2020-05-30              | 2020-05-31             | 2020-05-31              |
    And The list contains 3 competitions
