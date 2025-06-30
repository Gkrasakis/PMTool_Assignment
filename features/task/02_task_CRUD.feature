@tsk02
@Negative

Feature: Task Management

Background:
    Given I am on the login page of PMtool
    When I am logged in as a valid user registered before
    And I am on the Dashboard page of PMtool
    And I click the create button
    And I am on the createProject page
    And I enter Test_PR_task02 as project name and Project_with_tasks02 as description
    And I click the create project button
    And I should see Test_PR_task02 and Project_with_tasks02 in the project list

Scenario: Fail to create a new task with invalid details
    When I click the add task button located in Test_PR_task02
    And I am on the createTask page of PMtool
    And I insert empty Summary, Description and label
    And I click the create task button
    Then I should see an error message saying Summary and label are required
    