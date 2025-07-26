from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, random, string

############################## Feature: User Management-registration ##############################

@given("I am on the registration page")
def test_step(context):
    context.browser.get("https://pm-tool-e63fa77e3353.herokuapp.com/signup")

# 01_user_management #############################################################################
@when("I enter name, email, password, company and address")
def test_step(context):
    # Generating a random name
    username = "tester_" + ''.join(random.choices(string.digits, k=4))
    # Creating a matching email using that name
    email = f"{username}@example.com"
    # Choosing a password
    password = "TestPmTool!@1234"
    
    # Save email and password to file to make them global values for login step
    with open("last_registered_user.txt", "w") as file:
        file.write(f"{email},{password}")
        
    # Values saved in context so can be used later 
    context.generated_name = username
    context.generated_email = email
    context.generated_password = password
    
    # Fill the form in the browser with above values
    context.browser.find_element(By.ID, "fullName").send_keys(username)
    context.browser.find_element(By.ID, "email").send_keys(email)
    context.browser.find_element(By.ID, "password").send_keys(password)
    context.browser.find_element(By.ID, "company").send_keys("Holistic Computational Environments for Adaptive Software Solutions")
    context.browser.find_element(By.ID, "address").send_keys(
        "Global Technology Innovation Park, Tower C  Level 18, 9500 Continental Enterprise Boulevard ,Innovation District, Geneva Metropolitan Region, Switzerland, 1205  EU Tech Zone")
    # here i go with a long address to check length
    # Print what was used in terminal
    print(f"Registered with name: {username}, email: {email}")
# 01_user_management #############################################################################

# 02_user_management #############################################################################
# reuse @given("I am on the registration page")
@when("I enter name, email and password")
def test_step(context):
    # Generating a random name
    username = "tester_" + ''.join(random.choices(string.digits, k=4))
    # Creating a matching email using that name
    email = f"{username}@example.com"
    # Choosing a password
    password = "TestPmTool!@1234"
    
    # Save email and password to file to make them global values for login step
    with open("last_registered_user.txt", "w") as file:
        file.write(f"{email},{password}")
        
    # Values saved in context so can be used later 
    context.generated_name = username
    context.generated_email = email
    context.generated_password = password
    
    # Fill the form in the browser with above values
    context.browser.find_element(By.ID, "fullName").send_keys(username)
    context.browser.find_element(By.ID, "email").send_keys(email)
    context.browser.find_element(By.ID, "password").send_keys(password)
    
    # Print what was used in terminal
    print(f"Registered with name: {username}, email: {email}")

# 02_user_management ############################################################################# 

# 03_user_management #############################################################################
# reuse @given("I am on the registration page")
@when("I enter email and password")
def test_step(context):
    # Generating a random name
    username = "tester_" + ''.join(random.choices(string.digits, k=4))
    # Creating a matching email using that name
    email = f"{username}@example.com"
    # Choosing a password
    password = "TestPmTool!@1234"
    
    # Save email and password to file to make them global values for login step
    with open("last_registered_user.txt", "w") as file:
        file.write(f"{email},{password}")
        
    # Values saved in context so can be used later 
    context.generated_name = username
    context.generated_email = email
    context.generated_password = password
    
    # Fill the form in the browser with above values
    context.browser.find_element(By.ID, "email").send_keys(email)
    context.browser.find_element(By.ID, "password").send_keys(password)
# 03_user_management ############################################################################# 

# 04_user_management #############################################################################
# reuse @given("I am on the registration page") 
@when("I fill in name, invalid email and password")
def test_step(context):
    # Generating a random name
    username = "tester_" + ''.join(random.choices(string.digits, k=4))
    # Creating a matching email using that name
    email = f"{username}example.com" # removing @
    # Choosing a password
    password = "TestPmTool!@1234"
    
    # Save email and password to file to make them global values for login step
    with open("last_registered_user.txt", "w") as file:
        file.write(f"{email},{password}")
        
    # Values saved in context so can be used later 
    context.generated_name = username
    context.generated_email = email
    context.generated_password = password
    
    # Fill the form in the browser with above values
    context.browser.find_element(By.ID, "fullName").send_keys(username)
    context.browser.find_element(By.ID, "email").send_keys(email)
    context.browser.find_element(By.ID, "password").send_keys(password)
    # Print what was used in terminal
    print(f"Registered with name: {username}, email: {email}")
# 04_user_management ############################################################################# 

# 05_user_management #############################################################################
# reuse @given("I am on the registration page")
@when("I fill in name and email")
def test_step(context):
    # Generating a random name
    username = "tester_" + ''.join(random.choices(string.digits, k=4))
    # Creating a matching email using that name
    email = f"{username}@example.com" # removing @
    
    # Save email and password to file to make them global values for login step
    with open("last_registered_user.txt", "w") as file:
        file.write(f"{email}")

    # Values saved in context so can be used later 
    context.generated_name = username
    context.generated_email = email
    
    # Fill the form in the browser with above values
    context.browser.find_element(By.ID, "fullName").send_keys(username)
    context.browser.find_element(By.ID, "email").send_keys(email)   
# 05_user_management #############################################################################

# globally available #############################################################################

@when("I click the register button")
def test_step(context):
    # Using CSS selector for smart labels find a <button> with type = 'submit'
    button = context.browser.find_element(By.CSS_SELECTOR, "form button[type='submit']")
    button.click()
    time.sleep(2)  # Optional: let the redirect happen
    
@then("I should be redirected to the verification page")
def test_step(context):
    # Check URL contains '/login' or expected element is present
    assert "/verifyAccount" in context.browser.current_url, "redirected to the verification page"
    print(f"Registration worked for {context.generated_email}")

@then("I should see a name error message")
def test_step(context):
    # Wait for the error message related to the name field
    errors = context.browser.find_elements(By.CLASS_NAME, "invalid-feedback")
    for error in errors:
        if "This field is required" in error.text:
            return  
    # If not found, raise an error
    assert False, "Expected 'This field is required' message but it was not found"
    
@then("I should see a email error message")
def test_step(context):
    # Wait for the error message related to the name field 
    errors = context.browser.find_elements(By.CLASS_NAME, "invalid-feedback")
    for error in errors:
        if "Invalid email format" in error.text:
            return  
    # If not found, raise an error
    assert False, "Expected 'Invalid email format' message but it was not found"
    
@then("I should see a password error message")
def test_step(context):
    # Wait for the error message related to the name field 
    errors = context.browser.find_elements(By.CLASS_NAME, "invalid-feedback")
    for error in errors:
        if "This field is required" in error.text:
            return  
    # If not found, raise an error
    assert False, "Expected 'This field is required' message but it was not found"    
    
# globally available #############################################################################   
    
############################## Feature: User Management-registration ##############################




############################### Feature: User Management-login #####################################

@given("I am on the login page")
def test_step(context):
    context.browser.get("https://pm-tool-e63fa77e3353.herokuapp.com/login")
    
# 06_user_management ############################################################################# 
# reuse @given("I am on the login page")

@when("I enter registered email and password")
def test_step(context):
    context.browser.find_element(By.ID, "email").send_keys("tester_0160@example.com")
    context.browser.find_element(By.ID, "password").send_keys("TestPmTool!@1234")
# 06_user_management ############################################################################# 

# 07_user_management #############################################################################
# reuse @given("I am on the login page")

@when("I enter valid email and incorrect password")
def test_step(context):
    context.browser.find_element(By.ID, "email").send_keys("tester_0160@example.com")
    context.browser.find_element(By.ID, "password").send_keys("12341412rfdsFF2`!") # using password that does not match account
# 07_user_management #############################################################################

# 08_user_management #############################################################################
# reuse @given("I am on the login page")

@when("I enter unregistered email and any password")
def test_step(context):
    # using unregistered email and a random password 
    context.browser.find_element(By.ID, "email").send_keys("tester_unregistered@example.com")
    context.browser.find_element(By.ID, "password").send_keys("12341412rfdsFF2`!") 
# 08_user_management #############################################################################

# 09_user_management #############################################################################
# reuse @given("I am on the login page")
@when("I click the login button without entering credentials")
def test_step(context):
    button = context.browser.find_element(By.CSS_SELECTOR, "form button[type='submit']")
    button.click()
    time.sleep(2)  # Optional: let the redirect happen
    
@then("I should see required field error messages")
def test_step(context):
    # Wait for the error message related to the name field 
    errors = context.browser.find_elements(By.CLASS_NAME, "invalid-feedback")
    for error in errors:
        if "Invalid login info" in error.text:
            return  
    # If not found, raise an error
    assert False, "Expected 'Invalid login info' message but it was not found"   

# 09_user_management #############################################################################

# globally available #############################################################################   
@when("I click the login button")
def test_step(context):
    button = context.browser.find_element(By.CSS_SELECTOR, "form button[type='submit']")
    button.click()
    time.sleep(2)  # Optional: let the redirect happen

@then("I should be redirected to the dashboard page")
def test_step(context):
    # Check URL contains '/dashboard' or expected element is present
    assert "/dashboard" in context.browser.current_url, "redirected to the dashboard page"

@then("I should see a login error message")
def test_step(context):
    # Wait for the error message related to the name field 
    errors = context.browser.find_elements(By.CLASS_NAME, "invalid-feedback")
    for error in errors:
        if "Invalid login info" in error.text:
            return  
    # If not found, raise an error
    assert False, "Expected 'Invalid login info' message but it was not found"   
# globally available #############################################################################   

# ############################## Feature: User Management-login ######################################