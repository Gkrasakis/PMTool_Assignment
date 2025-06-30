# PM Tool Test Automation

## How to Run

1. Install Python 3 and Chrome
2. Install dependencies: `pip install -r requirements.txt`
3. Run tests: 
    to run all tests in folder --> `python -m behave feature/user` 
    to run all tests ---> `python -m behave`
    to run a single feature ---> `python -m behave feature/user/login.feature`
    to run multiple specific features --> `python -m behave feature/user/login.feature feature/project/create_project.feature` 
                                          `python -m behave --tags="@tsk01 or @tsk02 or @tsk03 or @tsk04"`


My suggestion is to start with user module then with project and at last task module
Please, after running project or task, delete any leftovers that may remain in the application so that it runs correctly. There might be conflicts otherwise

There is a results.txt that displays the list of feature/s that passed or failed after one run 
also screenshot dir is for when there is a failed test case 

