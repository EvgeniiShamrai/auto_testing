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
