Feature: List all competitions of a category
  In order to find out the competitions about topics we like the most
  As a user
  I want to list all the competitions that belong to a category
  Background: There are 2 competitions of a category registered by same user
    Given Exists a user "user" with password "password"
    And Exists a category "category1" with description "category1 description"
    And Exists a category "category2" with description "category2 description"

  Scenario: List all categories
    Given I login as user "user" with password "password"
    When I list categories
    Then I'm viewing a list containing all the categories
      | name       | description           |
      | category1  | category1 description |
      | category2  | category2 description |