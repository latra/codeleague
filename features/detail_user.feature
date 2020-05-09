Feature: Detail user
  In order to view our personal information
  As a user
  I want to be able to know ... about my profile

  Background: There is a registered user
    Given Exists a user "user" with password "password"

   Scenario: Show user information
     Given I login as user "user" with password "password"
     When I visit my profile
     Then I'm at "accounts/u/1/"
     Then I view all of my profile information
      | name  |
      | user  |