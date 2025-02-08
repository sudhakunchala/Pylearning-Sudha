import pytest
import allure
import requests


@allure.title("create booking CRUD")
@allure.description("TC#1-Verify the create booking")
@pytest.mark.crud
def test_create_booking_positive():
    # to make request
    #  URL
    # Method-Post
    # Headers-Content-Type=application/json
    # payload/data/
    base_url = "https://restful-booker.herokuapp.com/"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,  # in Python true should be start with capital T
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.post(url=URL, headers=headers, json=payload)
    assert response.status_code == 200

    responseData = response.json()

    assert responseData["bookingid"] is not None
    assert responseData["bookingid"] > 0
    assert type(responseData["bookingid"]) == int
