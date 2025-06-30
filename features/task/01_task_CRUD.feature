@tsk01
@Positive

Feature: Task Management

Background:
    Given I am on the login page of PMtool
    When I am logged in as a valid user registered before
    And I am on the Dashboard page of PMtool
    And I click the create button
    And I am on the createProject page
    And I enter Test_PR_task01 as project name and Project_with_tasks01 as description
    And I click the create project button
    And I should see Test_PR_task01 and Project_with_tasks01 in the project list

Scenario: Create a new task with valid details
    When I click the add task button located in Test_PR_task01
    And I am on the createTask page of PMtool
    And I insert valid Summary task01, Description 1st task and label testing
    And I click the create task button
    And I am on the tasks page of PMtool
    Then I should see task01 task list