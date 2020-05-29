# -*- coding: utf-8 -*-
import pytest
import requests
import json
import jsonpath
import base64
# урлы используемые в тестом
url_auth_sign_in = "https://1"
url_auth_refresh = "https://2"

# переменные используемые в тестом
empty_input = ""
email_admin = "admin@test.com"
email_manager = "manager@test.com"
email_technician = "technician@test.com"
email_wrong_admin = "admin_test.com"
test_password = "111111"


# Method for make tests more readable. This method cut off all excess parts of response.
def parse_and_decode_token(token):
    # Cut first symbol in string
    token = token[2:]
    # Revers string
    token = token[::-1]
    # Cut all symbols before chosen(include)
    token = token[token.find(".") + 1:]
    token = token[::-1]
    # Add "==" for make string able to decode! Amazing mental F#@$k from Python!
    token = token + "=="
    # Decoding clean part for parse ROLE of user
    token2 = base64.b64decode(token)
    token2 = token2.decode('utf-8')
    return token2


@pytest.mark.order2
@pytest.mark.usefixtures("make_dict_cred")
@pytest.mark.parametrize("user_email, user_password", [
    (empty_input, empty_input),
    (empty_input, test_password),
    (email_admin, empty_input),
    (email_wrong_admin, test_password)
])
def test_sign_in_negative_getting_tokens(user_email, user_password, make_dict_cred):
    url = url_auth_sign_in
    response = requests.post(url, make_dict_cred, verify=False)

    assert response.status_code == 401, "Ups! We got token when use wrong credentials! "


@pytest.mark.order1
@pytest.mark.usefixtures("make_dict_cred")
@pytest.mark.parametrize("user_email, user_password", [
    (email_admin, test_password)
])
def test_sign_in_getting_tokens_admin(user_email, user_password, make_dict_cred):
    url = url_auth_sign_in
    # Fetch header from response
    response = requests.post(url, make_dict_cred, verify=False)
    # Parse response to JSON format
    response_json = json.loads(response.text)
    # Pick tokens using jsonpath
    token = str(jsonpath.jsonpath(response_json, "token"))
    refresh_token = str(jsonpath.jsonpath(response_json, "refresh_token"))
    # Checking for control
    assert token != "", "Token is wrong! None symbol in token!"
    assert refresh_token != "", "Token is wrong! None symbol in token!"

    token2 = parse_and_decode_token(token)

    assert "MANAGER_ROLE" in token2, "Manager has wrong role! No role MANAGER!"
    assert "ADMIN_RULE" in token2, "Admin has wrong role! No role ADMIN!"


@pytest.mark.order1
@pytest.mark.usefixtures("make_dict_cred")
@pytest.mark.parametrize("user_email, user_password", [
    (email_manager, test_password)
])
def test_sign_in_getting_tokens_manager(user_email, user_password, make_dict_cred):
    url = url_auth_sign_in

    response = requests.post(url, make_dict_cred, verify=False)

    response_json = json.loads(response.text)

    token = str(jsonpath.jsonpath(response_json, "token"))
    refresh_token = str(jsonpath.jsonpath(response_json, "refresh_token"))

    assert len(token) != 0, "Token is wrong! None symbol in token!"
    assert len(refresh_token) != 0, "Token is wrong! None symbol in token!"
    assert len(token) < 1000, "Token is wrong! Token has more then 1000 symbols!"
    assert len(refresh_token) < 1000, "Token is wrong! Token has more then 1000 symbols!"

    token2 = parse_and_decode_token(token)

    assert "MANAGER_ROLE" in token2, "Manager has wrong role! No MANAGER role!"


@pytest.mark.order1
@pytest.mark.usefixtures("make_dict_cred")
@pytest.mark.parametrize("user_email, user_password", [
    (email_technician, test_password)
])
def test_sign_in_getting_tokens_technician(user_email, user_password, make_dict_cred):
    url = url_auth_sign_in

    response = requests.post(url, make_dict_cred, verify=False)

    response_json = json.loads(response.text)

    token = str(jsonpath.jsonpath(response_json, "token"))
    refresh_token = str(jsonpath.jsonpath(response_json, "refresh_token"))

    assert len(token) != 0, "Token is wrong! None symbol in token!"
    assert len(refresh_token) != 0, "Token is wrong! None symbol in token!"
    assert len(token) < 1000, "Token is wrong! Token has more then 1000 symbols!"
    assert len(refresh_token) < 1000, "Token is wrong! Token has more then 1000 symbols!"

    token2 = parse_and_decode_token(token)

    assert "UNDERFINED_ROLE" in token2, "Role for technician??? Technician has wrong role!"


@pytest.mark.order1
@pytest.mark.usefixtures("make_refresh_token")
@pytest.mark.parametrize("user_email, user_password, user_url_auth_sign_in", [
    (email_admin, test_password, url_auth_sign_in)
])
def test_refresh_token_for_get_tokens(user_email, user_password, user_url_auth_sign_in, make_refresh_token):
    url = url_auth_refresh
    response = requests.post(url, make_refresh_token, verify=False)

    response_json = json.loads(response.text)

    token = str(jsonpath.jsonpath(response_json, "token"))
    refresh_token = str(jsonpath.jsonpath(response_json, "refresh_token"))

    assert len(token) != 0, "Token is wrong! None symbol in token!"
    assert len(refresh_token) != 0, "Token is wrong! None symbol in token!"
    assert len(token) < 1000, "Token is wrong! Token has more then 1000 symbols!"
    assert len(refresh_token) < 1000, "Token is wrong! Token has more then 1000 symbols!"


@pytest.mark.order4
@pytest.mark.usefixtures("make_broken_refresh_token")
def test_use_wrong_refresh_token_for_get_tokens(make_broken_refresh_token):
    url = url_auth_refresh
    response = requests.post(url, make_broken_refresh_token, verify=False)

    assert response.status_code == 401, "Ups! We got token when use wrong refresh token!!!"

# pytest test_token_admin.py
# pytest --alluredir=/Users/alexandrvolchkov/Documents/Automation/APIsaas2/results
# allure serve /Users/alexandrvolchkov/Documents/Automation/APIsaas2/results
