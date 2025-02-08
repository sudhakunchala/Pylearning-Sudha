def test_addition():
    assert 1+1 == 2

# in Pytest the file should start with test_
# method should start with test_
# assert keyword  is used to validate test conditions
# if assert == true, then test case will get passed
# to run the test case in the terminal, we have to type pytest, it will fetch the file and run
# to get help , we can use pytest -h in the terminal
# to run a specific test case  we have to specify the path, pytest Pytest_API_Automation/test_lab001.py
def test_subtraction():
    assert 2-1 == 1