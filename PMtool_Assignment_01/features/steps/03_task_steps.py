from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.alert import Alert
import time, random, string

############################### Feature: Task Management CRUD #####################################

# 01_project_CRUD #############################################################################   
# reuse from project py
# @given("I am on the login page of PMtool")
# @when("I am logged in as a valid user registered before")
# @when("I am on the Dashboard page of PMtool")
# @when("I click the create button")
# @when("I am on the createProject page") 

@when("I enter Test_PR_task01 as project name and Project_with_tasks01 as description")
def test_step(context):
    context.browser.find_element(By.ID, "name").send_keys("Test_PR_task01")
    context.browser.find_element(By.ID, "description").send_keys("Project_with_tasks01")

# reuse @when("I click the create project button")
  
@when("I should see Test_PR_task01 and Project_with_tasks01 in the project list")
def test_step(context):
    cards = context.browser.find_elements(By.CLASS_NAME, "card-content")
    found = any("Test_PR_task01" in card.text and "Project_with_tasks01" in card.text for card in cards)
    assert found, "Project not found"

@when("I click the add task button located in Test_PR_task01")
def test_step(context):
    # Reason that cards is used, because need to be specific in wich card will go to edit for what project and not the first available
    cards = context.browser.find_elements(By.CLASS_NAME, "card-content")
    for card in cards:
        # IF you find in card.test Test_PR01 then try else give error
        if "Test_PR_task01" in card.text:
            try:
                button = context.browser.find_element(By.ID, "btn_add_task")  
                button.click()
                time.sleep(2)  # Optional: let the redirect happen
                return
            except:
                assert False, "'add task' button not found in card containing Test_PR_task01"
    assert False, "Project card for 'Test_PR_task01' not found"

@when("I am on the createTask page of PMtool")
def test_step(context):
    current_url = context.browser.current_url
    assert current_url.endswith("/createTask")  # because the url contains specific uuid for each project need to check only the last part of url 


@when("I insert valid Summary task01, Description 1st task and label testing")
def test_step(context):
    context.browser.find_element(By.ID, "summary").send_keys("task01")
    context.browser.find_element(By.ID, "description").send_keys("1st task")
    context.browser.find_element(By.ID, "search_input").click()
    # here i need to find all tags that are on dropdown menu
    tags = context.browser.find_elements(By.CLASS_NAME, "option")
    # Look through each tag and click the one called "testing"
    for tag in tags:
        if tag.text.strip().lower() == "testing":
            tag.click()
            break
        
    time.sleep(1)
    # make a click to body to close dropdown because submit is not clickable
    context.browser.find_element(By.ID, "root").click()
    
    
@when("I click the create task button")
def test_step(context):
    # Using CSS selector for smart labels find a <button> with type = 'submit'
    create_button = context.browser.find_element(By.CSS_SELECTOR, "form button[type='submit']")
    create_button.click()
    time.sleep(2)

@when("I am on the tasks page of PMtool")
def test_step(context):
    current_url = context.browser.current_url
    assert current_url.endswith("/tasks")  # because the url contains specific uuid for each project need to check only the last part of url 

@then("I should see task01 task list")
def test_step(context):
    titles = context.browser.find_elements(By.ID, "card_title")
    descs = context.browser.find_elements(By.ID, "card_description")
    found = any(
        "task01" in title.text and "1st task" in description.text for title, description in zip(titles, descs))
    # so i do not forget zip will group the elements from the three lists together so for each task, can access its title, description, and label.
    assert found, "task01 not found"
# 01_task_CRUD.feature ############################################################################# 

# 02_task_CRUD.feature ############################################################################# 
# reuse from project py
# @given("I am on the login page of PMtool")
# @when("I am logged in as a valid user registered before")
# @when("I am on the Dashboard page of PMtool")
# @when("I click the create button")
# @when("I am on the createProject page") 

@when("I enter Test_PR_task02 as project name and Project_with_tasks02 as description")
def test_step(context):
    context.browser.find_element(By.ID, "name").send_keys("Test_PR_task02")
    context.browser.find_element(By.ID, "description").send_keys("Project_with_tasks02")

# reuse @when("I click the create project button")
  
@when("I should see Test_PR_task02 and Project_with_tasks02 in the project list")
def test_step(context):
    cards = context.browser.find_elements(By.CLASS_NAME, "card-content")
    found = any("Test_PR_task02" in card.text and "Project_with_tasks02" in card.text for card in cards)
    assert found, "Project not found"

@when("I click the add task button located in Test_PR_task02")
def test_step(context):
    # Reason that cards is used, because need to be specific in wich card will go to edit for what project and not the first available
    cards = context.browser.find_elements(By.CLASS_NAME, "card-content")
    for card in cards:
        # IF you find in card.test Test_PR01 then try else give error
        if "Test_PR_task02" in card.text:
            try:
                button = context.browser.find_element(By.ID, "btn_add_task")  # a[href="/createProject"]
                button.click()
                time.sleep(2)  # Optional: let the redirect happen
                return
            except:
                assert False, "'add task' button not found in card containing Test_PR_task02"
    assert False, "Project card for 'Test_PR_task02' not found"

# reuse
# @when("I am on the createTask page of PMtool")

@when("I insert empty Summary, Description and label")
def test_step(context):
    context.browser.find_element(By.ID, "summary").send_keys("")
    context.browser.find_element(By.ID, "description").send_keys("")
    
# reuse
# @when("I click the create task button")

@then("I should see an error message saying Summary and label are required")
def test_step(context):
    # Wait for the error message related to the name field
    errors = context.browser.find_elements(By.CLASS_NAME, "invalid-feedback")
    for error in errors:
        if "This field is required" in error.text:
            return  
    # If not found, raise an error
    assert False, "This field is required for Summary and description"
# 02_task_CRUD.feature ############################################################################# 

# 03_task_CRUD.feature ############################################################################# 
# reuse 
# @given("I am on the login page of PMtool")
# @when("I am logged in as a valid user registered before")
# @when("I am on the Dashboard page of PMtool")
# @when("I click the create button")
# @when("I am on the createProject page") 
# @when("I enter Test_PR_task02 as project name and Project_with_tasks02 as description")
# @when("I enter Test_PR_task02 as project name and Project_with_tasks02 as description")
# @when("I click the create project button")
# @when("I should see Test_PR_task02 and Project_with_tasks02 in the project list")
# @when("I click the add task button located in Test_PR_task02")
# @when("I am on the createTask page of PMtool")

@when("I insert task_unedited in Summary, task before edit in Description")
def test_step(context):
    context.browser.find_element(By.ID, "summary").send_keys("task_unedited")
    context.browser.find_element(By.ID, "description").send_keys("task before edit")

# reuse
# @when("I click the create task button")

@when("I see task_unedited in task list")
def test_step(context):
    titles = context.browser.find_elements(By.ID, "card_title")
    descs = context.browser.find_elements(By.ID, "card_description")
    found = any(
        "task_unedited" in title.text and "task before edit" in description.text for title, description in zip(titles, descs))
    # so i do not forget zip will group the elements from the three lists together so for each task, can access its title, description, and label.
    assert found, "task_unedited not found"
    
@when("I click the edit button located in task_unedited")
def test_step(context):
    # Reason that cards is used, because need to be specific in wich card will go to edit for what project and not the first available
    titles = context.browser.find_elements(By.ID, "card_title")
    for title in titles:
        # IF you find in card.test Test_PR01 then try else give error
        if "task_unedited" in title.text:
            try:
                button = context.browser.find_element(By.ID, "btn_update_task") 
                button.click()
                time.sleep(2)  # let the redirect happen
                return
            except:
                assert False, "'edit task' button not found in card containing task_unedited"
    assert False, "Task card for 'task_unedited' not found"
    
@when("I am on the update page of tasks")
def test_step(context):
    current_url = context.browser.current_url
    assert current_url.endswith("/update")  # because the url contains specific uuid for each project need to check only the last part of url 
    
@when("I change to task_edited in Summary, task after edit in Description")
def test_step(context):
    # this is for summary of task
    task_summary_field = context.browser.find_element(By.ID, "summary")
    task_summary_field.clear()  
    task_summary_field.send_keys("task_edited")
    
    #  this is for description of task
    task_description_field = context.browser.find_element(By.ID, "description")
    task_description_field.clear()  
    task_description_field.send_keys("task after edit")

@when("I click the update task button")
def test_step(context):
    # Using CSS selector for smart labels find a <button> with type = 'submit'
    create_button = context.browser.find_element(By.CSS_SELECTOR, "form button[type='submit']")
    create_button.click()
    time.sleep(2)

# reuse
# I am on the tasks page of PMtool

@then("I can locate task_edited and task after edit in task list")
def test_step(context):
    titles = context.browser.find_elements(By.ID, "card_title")
    descs = context.browser.find_elements(By.ID, "card_description")
    found = any(
        "task_edited" in title.text and "task after edit" in description.text for title, description in zip(titles, descs))
    # so i do not forget zip will group the elements from the three lists together so for each task, can access its title, description, and label.
    assert found, "task_edited not found"

# 03_task_CRUD.feature ############################################################################# 

# 04_task_CRUD.feature ############################################################################# 
# reuse 
# @given("I am on the login page of PMtool")
# @when("I am logged in as a valid user registered before")
# @when("I am on the Dashboard page of PMtool")
# @when("I click the create button")
# @when("I am on the createProject page") 
# @when("I enter Test_PR_task02 as project name and Project_with_tasks02 as description")
# @when("I enter Test_PR_task02 as project name and Project_with_tasks02 as description")
# @when("I click the create project button")
# @when("I should see Test_PR_task02 and Project_with_tasks02 in the project list")
# @when("I click the add task button located in Test_PR_task02")
# @when("I am on the createTask page of PMtool")

@when("I insert task_toTrash in Summary, task for del in Description")
def test_step(context):
    context.browser.find_element(By.ID, "summary").send_keys("task_toTrash")
    context.browser.find_element(By.ID, "description").send_keys("task for del")

# reuse
# @when("I click the create task button")

@when("I see task_toTrash in task list")
def test_step(context):
    titles = context.browser.find_elements(By.ID, "card_title")
    descs = context.browser.find_elements(By.ID, "card_description")
    found = any(
        "task_toTrash" in title.text and "task for del" in description.text for title, description in zip(titles, descs))
    # so i do not forget zip will group the elements from the three lists together so for each task, can access its title, description, and label.
    assert found, "task_toTrash not found"
    
@when("I click the delete button located in task_toTrash")
def test_step(context):
#     # Need to find all task cards first
    cards = context.browser.find_elements(By.CLASS_NAME, "card")    
    for card in cards:
        try:
            # Then i need to check for the title and desc inside each card 
            title = card.find_element(By.ID, "card_title").text
            description = card.find_element(By.ID, "card_description").text
            # Trying to find the one need to be deleted first 
            if title == "task_toTrash" and description == "task for del":
            # Now i found the card need to find the delete button inside card>cardtitle/card_description>task_toTrash>btn_delete_task
                delete_button = card.find_element(By.ID, "btn_delete_task")
                delete_button.click()
                time.sleep(1)
                return # if i found the button and click it need to exit
        except Exception as e:
            print("error")
    assert False, "Task card for task_toTrash not found"
    
    
    
    # # Reason that cards is used, because need to be specific in wich card will go to edit for what project and not the first available
    # titles = context.browser.find_elements(By.ID, "card_title")
    # for title in titles:
    #     # IF you find in card.test Test_PR01 then try else give error
    #     if "task_toTrash" in title.text:
    #         try:
    #             button = context.browser.find_element(By.ID, "btn_delete_task") 
    #             button.click()
    #             time.sleep(2)  # Optional: let the redirect happen
    #             return
    #         except:
    #             assert False, "'Delete task' button not found in card containing task_toTrash"
    # assert False, "Task card for 'task_toTrash' not found"
    
# @when("I click on the Delete button for Test_PR02")
# def test_step(context):
#     # Need to find all project cards first
#     cards = context.browser.find_elements(By.CLASS_NAME, "card")
#     for card in cards:
#         try:
#             # Then i need to check for the title and desc inside each card 
#             title = card.find_element(By.CLASS_NAME, "card-title").text
#             description = card.find_element(By.TAG_NAME, "p").text
#             # Trying to find the one need to be deleted first 
#             if title == "Test_PR02" and description == "Testing project02":
#                 # Now i found the card need to find the delete button inside card>cardtitle/p>Test_PR02>delete_project
#                 delete_button = card.find_element(By.ID, "delete_project")
#                 delete_button.click()
#                 time.sleep(1)
#                 return # if i found the button and click it need to exit
#         except Exception as e:
#             print("error")
#     assert False, "Project card for Test_PR02 not found"    
    

@when("I confirm the task deletion for task_toTrash")
def test_step(context):
    try:
        # Need to wait 5 sec for pop up to appear
        alert = WebDriverWait(context.browser, 5).until(EC.alert_is_present())
        assert "Are you sure you want to delete this task?" in alert.text
        alert.accept()  # else i can use dismiss to cancel the alert if i want to 
        time.sleep(2)
    except NoAlertPresentException:
        assert False, "No confirmation pop-up appeared"
        
# reuse 
# @when("I am on the tasks page of PMtool")
@then("I should not be able to locate task_toTrash and task for del in the task list")
def test_step(context):
    titles = context.browser.find_elements(By.ID, "card_title")
    descs = context.browser.find_elements(By.ID, "card_description")
    # Fail if any card contains both name and description
    for title,desc in zip(titles,descs):
        if "task_toTrash" in title.text and "task for del" in desc.text:
            assert False, "Task task_toTrash was still found in the task list"
# 04_task_CRUD.feature ############################################################################# 
            
############################### Feature: Task Management CRUD #####################################