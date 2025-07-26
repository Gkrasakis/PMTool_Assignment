@pr02
@Negative

Feature: Project Management

Background:
    Given I am on the login page of PMtool
    When I am logged in as a valid user registered before
    And I am on the Dashboard page of PMtool
    And I click the create button
    And I am on the createProject page

Scenario: Fail to create a new project with empty project name
    When I leave blank project name and a project with noname as description
    And I click the create project button
    Then I should see this field is required error for the missing project name