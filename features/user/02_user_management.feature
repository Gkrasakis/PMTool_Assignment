@user02
@Positive

Feature: User Management-registration

  Scenario: Register with name, email, and password only
    Given I am on the registration page
    When I enter name, email and password
    And I click the register button
    Then I should be redirected to the verification page