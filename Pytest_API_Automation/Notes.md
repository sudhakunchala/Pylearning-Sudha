 import pytest
 to use mark annotation, need to use  @pytest.mark.smoke
# we can divide testcases using this mark and run them
# to run in the terminal , pytest -m "smoke" path
# to ru the report first install allure-pytest pip install allure-pytest
#import allure
to run all the test cases in the terminal type : pytest Pytest_API_Automation/test_lab004.py- this path we will get form the file, right click and click on content , it will copy
to run allure reports, we need to do upper one and --alluredir=allure_result_folder  it will create allure result folder
to generate report : allure serve allure_result_folder
take the ip address and paste it in the browser
- if you want the response data should come in the terminal, you have to use  pytest Pytest_API_Automation/test_lab004.py --alluredir=allure_result_folder -s
# How to add request module to the project
Request module: (in Java it is rest assured)
1. Module in python --- is a package or library contains functions which we can use easily
2. ex: pytest, allure, time, math, csv
3. to make different request we use request module
4. Install request library using pip install requests
## what to do
1. import pytest
2. import allure
3. import requests
4. 