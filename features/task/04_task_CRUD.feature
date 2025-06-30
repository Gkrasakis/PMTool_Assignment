@tsk04
@Positive

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
    And I click the add task button located in Test_PR_task02
    And I am on the createTask page of PMtool

Scenario: Delete already created task
    When I insert task_toTrash in Summary, task for del in Description
    And I click the create task button
    And I see task_toTrash in task list
    And I click the delete button located in task_toTrash
    And I confirm the task deletion for task_toTrash
    And I am on the tasks page of PMtool
    Then I should not be able to locate task_toTrash and task for del in the task list