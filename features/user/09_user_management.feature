@user09
@negative
Feature: User Management-login

  Scenario: Try to login without filling in any fields
    Given I am on the login page
    When I click the login button without entering credentials
    Then I should see required field error messages
