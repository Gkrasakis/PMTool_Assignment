@pr05
@Positive

Feature: Project Management

Background:
    Given I am on the login page of PMtool
    When I am logged in as a valid user registered before
    And I am on the Dashboard page of PMtool
    When I click the create button
    And I am on the createProject page
    
Scenario: Delete an existing project
    When I enter Test_PR02 as project name and Testing project02 as description
    And I click the create project button
    And I see Test_PR02 and description Testing project02 in the project list
    And I click on the Delete button for Test_PR02
    And I confirm the project deletion for Test_PR02
    And I am on the Dashboard page of PMtool
    Then I should not be able to locate Test_PR02 and Testing project02 in the project list