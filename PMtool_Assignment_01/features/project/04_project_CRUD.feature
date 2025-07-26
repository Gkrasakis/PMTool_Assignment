@pr04
@Negative

Feature: Project Management

Background:
    Given I am on the login page of PMtool
    When I am logged in as a valid user registered before
    And I am on the Dashboard page of PMtool
    And I see Test_PR01_edited and description edited project in the project list
    
Scenario: Edit an existing project blank name
    When I click on the Edit button for Test_PR01_edited
    And I am on the update page
    And I leave blank the name and description noname project
    And I click on the Update button
    Then I should see this field is required error for the missing project name