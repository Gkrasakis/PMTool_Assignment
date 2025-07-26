@user06
@positive

Feature: User Management-login

  Scenario: Login with valid email and password
    Given I am on the login page
    When I enter registered email and password
    And I click the login button
    Then I should be redirected to the dashboard page
