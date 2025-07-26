@user01
@Positive

Feature: User Management-registration

  Scenario: Register with name, email, password, company and address
    Given I am on the registration page
    When I enter name, email, password, company and address
    And I click the register button
    Then I should be redirected to the verification page