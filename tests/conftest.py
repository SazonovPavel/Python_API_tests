import pytest
import json
import requests

from data_for_test.data_cred_auth import *
# from data_for_test.data_rt_section_paragraph import DataTest


# This fixture is idea how make tests more readable and simple
@pytest.fixture()
def make_dict_cred(user_email, user_password):
    dict_cred = {
        "user_email": user_email,
        "user_password": user_password
    }
    return dict_cred


@pytest.fixture()
def make_refresh_token(user_email, user_password, user_url_auth_sign_in):
    dict_cred = {
        "user_email": user_email,
        "user_password": user_password
    }

    url = user_url_auth_sign_in

    response = requests.post(url, dict_cred, verify=False)
    response_json = json.loads(response.text)

    refresh_token = str(response_json["refresh_token"])

    good_refresh_token = {
        "refresh_token": refresh_token
    }
    return good_refresh_token


@pytest.fixture()
def make_broken_refresh_token():
    broken_refresh_token = {
        "refresh_token": "W Szczebrzeszynie chrząszcz brzmi w trzcinie I Szczebrzeszyn z tego słynie."
    }
    return broken_refresh_token


# Fixture for mock service ABFP
@pytest.fixture()
def make_dict_cred_for_new_service(test_comment, service_name):
    dict_cred = {
        "comment": test_comment,
        "name": service_name,
    }
    return dict_cred


# Fixture for mock service ABFP
@pytest.fixture()
def make_dict_cred_for_new_device(name, parent_id):
    dict_cred = {
        "name": name,
        "parentID": parent_id
    }
    return dict_cred


# Fixture for mock service ABFP
@pytest.fixture()
def make_dict_cred_for_new_user(name, email, password, roles, enable):
    dict_cred = {
        "username": name,
        "email": email,
        "password": password,
        "roles": roles,
        "enable": enable
    }
    return dict_cred


# report template management
@pytest.fixture(scope="function", autouse=True)
def get_new_jvt_token():
    dict_cred = {
        "user_email": email_admin,
        "user_password": cred_password
    }

    url = url_auth_for_sign_in

    response = requests.post(url, dict_cred, verify=False)
    response_json = json.loads(response.text)

    token = str(response_json["token"])

    token = {
        "X-ACCESS-TOKEN": token
    }
    return token
