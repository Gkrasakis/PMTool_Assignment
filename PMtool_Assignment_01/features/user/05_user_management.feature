@user05
@negative

Feature: User Management-registration

  Scenario: Try to register without a password
    Given I am on the registration page
    When I fill in name and email
    And I click the register button
    Then I should see a password error message