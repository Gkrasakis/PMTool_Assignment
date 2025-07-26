@tsk03
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

Scenario: Edit already created task
    When I insert task_unedited in Summary, task before edit in Description
    And I click the create task button
    And I see task_unedited in task list
    And I click the edit button located in task_unedited
    And I am on the update page of tasks
    And I change to task_edited in Summary, task after edit in Description
    And I click the update task button
    And I am on the tasks page of PMtool
    Then I can locate task_edited and task after edit in task list