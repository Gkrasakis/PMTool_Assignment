@pr03
@Positive

Feature: Project Management

Background:
    Given I am on the login page of PMtool
    When I am logged in as a valid user registered before
    And I am on the Dashboard page of PMtool
    When I click the create button
    And I am on the createProject page
    And I enter Test_PR01 as project name and Testing project01 as description
    And I click the create project button

Scenario: Edit an existing project
    When I should see Test_PR01 and Testing project01 in the project list
    And I click on the Edit button for Test_PR01
    And I am on the update page
    And I change the name to Test_PR01_edited and description to edited project
    And I click on the Update button
    Then I should see Test_PR01_edited and description edited project in the project list