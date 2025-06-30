from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

def before_all(context):
    print("before_all: starting browser")
    options = Options()
    # options.add_argument("--headless")  # Tells Chrome to run without showing the browser window  
    context.browser = webdriver.Chrome(options=options)
    #  in order to create a dir for reports if does not exist
    if not os.path.exists("reports"):
        os.makedirs("reports")
    
    with open("reports/results.txt", "w") as f:
        f.write("Test Results:\n")
        
def after_all(context):
    print("after_all: closing browser")
    context.browser.quit()

def after_scenario(context, scenario):
    # Prepare the result line
    status = "FAILED" if scenario.status == "failed" else "PASSED"
    result = f"{scenario.name}: {status}"

    print(result)
    
    # Append to the text file
    with open("reports/results.txt", "a") as f:
        f.write(result + "\n")
        
    if scenario.status == "failed":
        print("Scenario failed, taking screenshot")
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        context.browser.save_screenshot(f"screenshots/{scenario.name}.png")

print("environment.py loaded")


