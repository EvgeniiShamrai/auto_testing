# auto_testing
Project to study writing autotests in python

# Frequently used commands in autotesting
* Create a virtual environment : **python -m venv venv** 
* Add packages to a text document "requirements.txt" : **pip freeze > requirements.txt**
* Install all packages from the file "requirements.txt": **pip install -r requirements.txt**

# Rules for launching autotests pytest
### Rules for naming files, classes, and tests
* in all directories, Test searches for files that satisfy the test\_\*.py or \*\_test.py (that is , they start with test_ or end with _test and have an extension .py)
* inside all these files , it finds test functions according to the following rule:
  * all tests whose name begins with test that are outside of classes
  * all tests whose name starts with test inside classes whose name starts with 
    Test (and without the \_\_init\_\_ method inside the class)
* find all tests in the scripts/selenium_scripts directory: **pytest scripts/selenium_scripts**
* find and run all the tests in the file: **pytest test_user_interface.py**
* find a test named "test_register_new_user_parametrized" in the specified file in the specified directory and execute: **pytest scripts/drafts.py::test_register_new_user_parametrized**

# Running pytest tests via bash terminal
* Display the text output by the print() command: **pytest -s <name_executable_file.py>**
* Display the text output by the print() command with additional information: **pytest -s -v <name_executable_file.py>**
* Running the test with the desired marking: **pytest -s -v -m <name_marking_test> <name_executable_file.py>** -m running the test with the desired marking
* Running all tests not marked as `smoke`: **pytest -s -v -m "not smoke" <name_executable_file.py>**
* To run tests with different labels, you can use a logical OR: **pytest -s -v -m "smoke or regression" <name_executable_file.py>** 
* To run only smoke tests for Windows 10, you need to use the logical AND: *pytest -s -v -m "smoke and win10" <name_executable_file.py>**
* A command to run an expected failed test with the ability to display the messages specified in the reason parameter: **pytest -rx -v <name_executable_file.py>**
* Running tests from the command line using another browser: **pytest -s -v --browser_name=<name_browser> <name_executable_file.py>** 


# Skipping tests
To skip the test, use the decorator @pytest.mark.skip. At the same time, you do not need to make changes to the pytest.ini file
```
@pytest.mark.skip
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")
```

# Marking of the test
It is necessary to create a test.ini file in the root directory of the project.   In the file for explicitly prescribe the marking of tests.
``` 
[pytest]
markers =
    smoke: marker for smoke tests
    regression: marker for regression tests
```
For a test that has several markings in the pytest.ini file, you must specify them to register
```
[pytest]
markers =
    smoke: marker for smoke tests
    regression: marker for regression tests
    win10
```
# Rerun test
Install plugin pytest-rerunfailures in venv: **pip install pytest-rerunfailures**
To specify the number of restarts for each of the failed tests, you need to add a parameter to the command line: **"--reruns n", where n is the number of restarts.**
To shorten the log with the test results, use the parameter in the startup command **"--tb=line"**
Example of a command to restart tests: **pytest -v --tb=line --reruns 1 --browser_name=<name_browser> <name_executable_file.py>**