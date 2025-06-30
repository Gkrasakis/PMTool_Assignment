@user07
@negative
Feature: User Management-login

  Scenario: Login with incorrect password
    Given I am on the login page
    When I enter valid email and incorrect password
    And I click the login button
    Then I should see a login error message
