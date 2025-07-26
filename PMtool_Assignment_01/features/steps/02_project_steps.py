from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from selenium.webdriver.common.alert import Alert
import time, random, string

############################### Feature: Project Management CRUD #####################################

# 01_project_CRUD #############################################################################
@given("I am on the login page of PMtool")
def test_step(context):
    context.browser.get("https://pm-tool-e63fa77e3353.herokuapp.com/login")
    
@when("I am logged in as a valid user registered before")
def test_step(context):
    context.browser.find_element(By.ID, "email").send_keys("tester_0160@example.com")
    context.browser.find_element(By.ID, "password").send_keys("TestPmTool!@1234")
    context.browser.find_element(By.CSS_SELECTOR, "form button[type='submit']").click()
    time.sleep(2)

@when("I am on the Dashboard page of PMtool")
def test_step(context):
    # Check URL contains '/dashboard' or expected element is present
    assert "/dashboard" in context.browser.current_url, "redirected to the dashboard page"
    
@when("I click the create button")
def test_step(context):
    # Using CSS selector for smart labels find a <button> with a[href="/createProject"]
    create_button = context.browser.find_element(By.CSS_SELECTOR, 'a[href="/createProject"]')
    create_button.click()
    time.sleep(2) 

@when("I am on the createProject page")
def test_step(context):
    context.browser.get("https://pm-tool-e63fa77e3353.herokuapp.com/createProject")
  
@when("I enter Test_PR01 as project name and Testing project01 as description")
def test_step(context):
    context.browser.find_element(By.ID, "name").send_keys("Test_PR01")
    context.browser.find_element(By.ID, "description").send_keys("Testing project01")

@when("I click the create project button")
def test_step(context):
    # Using CSS selector for smart labels find a <button> with type = 'submit'
    button = context.browser.find_element(By.CSS_SELECTOR, "form button[type='submit']")
    button.click()
    time.sleep(2)  #  let the redirect happen
    
@then("I should see Test_PR01 and Testing project01 in the project list")
def test_step(context):
    cards = context.browser.find_elements(By.CLASS_NAME, "card-content")
    found = any("Test_PR01" in card.text and "Testing project01" in card.text for card in cards)
    assert found, "Project not found"
# 01_project_CRUD ###################################################################################

# 02_project_CRUD ###################################################################################
# reuse 
# @given("I am on the login page of PMtool")
# @when("I am logged in as a valid user registered before")
# @when("I am on the Dashboard page of PMtool")
# @when("I click the create button")
# @when("I am on the createProject page")

@when("I leave blank project name and a project with noname as description")
def test_step(context):
    context.browser.find_element(By.ID, "name").send_keys("")
    context.browser.find_element(By.ID, "description").send_keys("a project with noname")

# reuse @when("I click the create project button")

@then("I should see this field is required error for the missing project name")
def test_step(context):
    # Wait for the error message related to the name field 
    errors = context.browser.find_elements(By.CLASS_NAME, "invalid-feedback")
    for error in errors:
        if "This field is required" in error.text:
            return  
    # If not found, raise an error
    assert False, "Expected 'This field is required' message but it was not found" 
# 02_project_CRUD ###################################################################################

# 03_project_CRUD ###################################################################################
# reuse 
# @given("I am on the login page of PMtool")
# @when("I am logged in as a valid user registered before")
# @when("I am on the Dashboard page of PMtool")
# @when("I click the create button")
# @when("I am on the createProject page")   
# @when("I enter Test_PR01 as project name and Testing project01 as description")
# @when("I click the create project button")

# @then("I should see Test_PR01 and Testing project01 in the project list") as when
@when("I should see Test_PR01 and Testing project01 in the project list")
def test_step(context):
    cards = context.browser.find_elements(By.CLASS_NAME, "card-content")
    found = any("Test_PR01" in card.text and "Testing project01" in card.text for card in cards)
    assert found, "Project not found"
    
@when("I click on the Edit button for Test_PR01")
def test_step(context):
    # Reason that cards is used, because need to be specific in wich card will go to edit for what project and not the first available
    cards = context.browser.find_elements(By.CLASS_NAME, "card-content")
    for card in cards:
        # IF you find in card.test Test_PR01 then try else give error
        if "Test_PR01" in card.text:
            try:
                button = context.browser.find_element(By.ID, "btn_update_project")  # a[href="/createProject"]
                button.click()
                time.sleep(2)  # Optional: let the redirect happen
                return
            except:
                assert False, "'Edit' button not found in card containing Test_PR01"
    assert False, "Project card for 'Test_PR01' not found"
    
@when("I am on the update page")
def test_step(context):
    current_url = context.browser.current_url
    assert current_url.endswith("/update")  # because the url contains specific uuid for each project need to check only the last part of url 

@when("I change the name to Test_PR01_edited and description to edited project")
def test_step(context):
    # for project name
    name_field = context.browser.find_element(By.ID, "name")
    name_field.clear()  # at first i need to clear the field in order to insert new one 
    name_field.send_keys("Test_PR01_edited")
    
    # for project description
    desc_field = context.browser.find_element(By.ID, "description")
    desc_field.clear() # at first i need to clear the field in order to insert new one 
    desc_field.send_keys("edited project")

@when("I click on the Update button")
def test_step(context):
    # Using CSS selector for smart labels find a <button> with type = 'submit'
    button = context.browser.find_element(By.CSS_SELECTOR, "form button[type='submit']") 
    button.click()
    time.sleep(2)  # Optional: let the redirect happen

@then("I should see Test_PR01_edited and description edited project in the project list")
def test_step(context):
    cards = context.browser.find_elements(By.CLASS_NAME, "card-content")
    found = any("Test_PR01_edited" in card.text and "edited project" in card.text for card in cards)
    assert found, "Project not found"
# 03_project_CRUD ###################################################################################

# 04_project_CRUD ###################################################################################
# reuse 
# @given("I am on the login page of PMtool")
# @when("I am logged in as a valid user registered before")
# @when("I am on the Dashboard page of PMtool")  

@when("I see Test_PR01_edited and description edited project in the project list")
def test_step(context):
    cards = context.browser.find_elements(By.CLASS_NAME, "card-content")
    found = any("Test_PR01_edited" in card.text and "edited project" in card.text for card in cards)
    assert found, "Project not found"

@when("I click on the Edit button for Test_PR01_edited")
def test_step(context):
    # Reason that cards is used, because need to be specific in wich card will go to edit for what project and not the first available
    cards = context.browser.find_elements(By.CLASS_NAME, "card-content")
    for card in cards:
        # IF you find in card.test Test_PR01 then try else give error
        if "Test_PR01_edited" in card.text:
            try:
                button = context.browser.find_element(By.ID, "btn_update_project") 
                button.click()
                time.sleep(2)  # Optional: let the redirect happen
                return
            except:
                assert False, "'Edit' button not found in card containing Test_PR01_edited"
    assert False, "Project card for 'Test_PR01_edited' not found"

# reuse @when("I am on the update page")

@when("I leave blank the name and description noname project")
def test_step(context):
    # for project name
    name_field = context.browser.find_element(By.ID, "name")
    name_field.clear()  
    name_field.send_keys(" ")
    # for project description
    desc_field = context.browser.find_element(By.ID, "description")
    desc_field.clear() 
    desc_field.send_keys("noname project")
    context.browser.find_element(By.ID, "root").click()
# reuse 
# @when("I click on the Update button")
# @then("I should see this field is required error for the missing project name")
# 04_project_CRUD ###################################################################################

# 05_project_CRUD ###################################################################################
# reuse 
# @given("I am on the login page of PMtool")
# @when("I am logged in as a valid user registered before")
# @when("I am on the Dashboard page of PMtool")  
# @when("I click the create button")
# @when("I am on the createProject page")

@when("I enter Test_PR02 as project name and Testing project02 as description")
def test_step(context):
    context.browser.find_element(By.ID, "name").send_keys("Test_PR02")
    context.browser.find_element(By.ID, "description").send_keys("Testing project02")

# reuse 
# @when("I click the create project button")

@when("I see Test_PR02 and description Testing project02 in the project list")
def test_step(context):
    cards = context.browser.find_elements(By.CLASS_NAME, "card-content")
    found = any("Test_PR02" in card.text and "Testing project02" in card.text for card in cards)
    assert found, "Project not found"

@when("I click on the Delete button for Test_PR02")
def test_step(context):
    # Need to find all project cards first
    cards = context.browser.find_elements(By.CLASS_NAME, "card")
    for card in cards:
        try:
            # Then i need to check for the title and desc inside each card 
            title = card.find_element(By.CLASS_NAME, "card-title").text
            description = card.find_element(By.TAG_NAME, "p").text
            # Trying to find the one need to be deleted first 
            if title == "Test_PR02" and description == "Testing project02":
                # Now i found the card need to find the delete button inside card>cardtitle/p>Test_PR02>delete_project
                delete_button = card.find_element(By.ID, "delete_project")
                delete_button.click()
                time.sleep(1)
                return # if i found the button and click it need to exit
        except Exception as e:
            print("error")
    assert False, "Project card for Test_PR02 not found"
      
@when("I confirm the project deletion for Test_PR02")
def test_step(context):
    try:
        alert = WebDriverWait(context.browser, 5).until(EC.alert_is_present())
        assert "Are you sure you want to delete this project?" in alert.text
        alert.accept()  # Click OK
        time.sleep(2)
    except TimeoutException:
        assert False, "No confirmation pop-up appeared"
    
# reuse @when("I am on the Dashboard page of PMtool")

@then("I should not be able to locate Test_PR02 and Testing project02 in the project list")
def test_step(context):
    titles = context.browser.find_elements(By.CLASS_NAME, "card-title")
    descriptions = context.browser.find_elements(By.CLASS_NAME, "card-description") 

    for title, description in zip(titles, descriptions):
        if "Test_PR02" in title.text and "Testing project02" in description.text:
            assert False, "Project Test_PR02 and Testing project02 were still found in the project list."

    print("Project Test_PR02 and Testing project02 were not found, as expected.")
# 05_project_CRUD ###################################################################################

############################### Feature: Project Management CRUD #####################################