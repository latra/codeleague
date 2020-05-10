Feature: List all categories
  In order to have competitions filtered in some way
  As a user
  I want to list all the categories
  Background: There is a category and a registered user
    Given Exists a user "user" with password "password"
    And Exists a category "category1" with description "category1 description"
    And Exists a category "category2" with description "category2 description"

  Scenario: List all categories
    Given I login as user "user" with password "password"
    When I list categories
    Then I'm at "category/"
    Then I'm viewing a list containing all the categories
      | name       | description           |
      | category1  | category1 description |
      | category2  | category2 description |

  Scenario: Try to list all categories but not logged in
    Given I'm not logged in
    When I list categories
    Then Need to login to have "category/" link available