Feature: Detail user
  In order to view our personal information
  As a user
  I want to be able to know ... about my profile

  Background: There is a registered user
    Given Exists a user "user" with password "password"

  Scenario: Show user information
    Given I login as user "user" with password "password"
    When I visit profile of "user"
    Then I'm at "accounts/u/1/"
    Then I view profile of "user" information

  Scenario: Try to see our profile information but not logged in
    Given I'm not logged in
    When I want to view my profile details
    Then Need to login to have "accounts/u/1/" link available