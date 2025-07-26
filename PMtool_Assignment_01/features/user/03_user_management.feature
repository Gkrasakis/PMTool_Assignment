@user03
@negative

Feature: User Management-registration

  Scenario: Try to register without a name
    Given I am on the registration page
    When I enter email and password
    And I click the register button
    Then I should see a name error message