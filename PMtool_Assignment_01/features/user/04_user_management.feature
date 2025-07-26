@user04
@negative

Feature: User Management-registration

  Scenario: Try to register with invalid email
    Given I am on the registration page
    When I fill in name, invalid email and password
    And I click the register button
    Then I should see a email error message