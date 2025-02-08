# import pytest
# to use mark annotation, need to use  @pytest.mark.smoke
# we can divide testcases using this mark and run them
# to run in the terminal , pytest -m "smoke" path
# to ru the report first install allure-pytest pip install allure-pytest
#import allure
# to run all the test cases in the terminal type : pytest Pytest_API_Automation/test_lab004.py- this path we will get form the file, right click and click on content , it will copy
# to run allure reports, we need to do upper one and --alluredir=allure_result_folder  it will create allure result folder
#  to generate report : allure serve allure_result_folder
# take the ip address and paste it in the browser
import pytest
import allure
@pytest.mark.smoke
@allure.title("TC1- verify that 1 + 2 is 3")
@allure.description("This is smoke testing1")
def test_add():
    assert 1 +2 == 3

@pytest.mark.smoke
@allure.title("TC1- verify that 3-2 is 1")
@allure.description("This is smoke testing2")
def test_sub():
    assert 3-2 == 1

@pytest.mark.regression
@allure.title("TC1- verify that 2 * 2 is 4")
@allure.description("This is regression test")
def test_mul():
    assert 2*2 == 4

@pytest.mark.sanity
@allure.title("TC1- verify that 4/2 is 2")
@allure.description("This is sanity testing")
def test_div():
    assert 4/2 == 2

