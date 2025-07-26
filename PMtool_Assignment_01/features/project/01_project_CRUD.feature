@pr01
@Positive

Feature: Project Management

Background:
    Given I am on the login page of PMtool
    When I am logged in as a valid user registered before
    And I am on the Dashboard page of PMtool

Scenario: Create a new project with valid details
    When I click the create button
    And I am on the createProject page
    And I enter Test_PR01 as project name and Testing project01 as description 
    And I click the create project button
    Then I should see Test_PR01 and Testing project01 in the project list