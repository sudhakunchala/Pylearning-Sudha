import pytest
import allure
import requests

@allure.title("Test Get Request-RestFul Booker Project#1")
@allure.description("TC#1- verify GET request with id works")
@allure.tag("regression","p0","smoke")
@allure.testcase("TC#1")
@pytest.mark.smoke
def test_get_single_request_by_id():
    url= "https://restful-booker.herokuapp.com/booking/714"
    responseData = requests.get(url)
    print(responseData.json())
    assert responseData.status_code == 200