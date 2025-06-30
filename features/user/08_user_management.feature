@user08
@negative
Feature: User Management-login

  Scenario: Login with an unregistered email
    Given I am on the login page
    When I enter unregistered email and any password
    And I click the login button
    Then I should see a login error message
