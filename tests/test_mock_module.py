# -*- coding: utf-8 -*-
import pytest
import requests
# урлы используемые в тестом
url_user = "https://1"
url_devise = "https://2"
url_service = "https://3"

# Значения переменных используемых фикстурой
name_admin_for_fixture = "admin@1.com"
email_admin_for_fixture = "admin@2.com"
test_password_for_fixture = "test_password"
roles_value_for_fixture = "Admin, Manager"
enable_value_for_fixture = "true"


@pytest.mark.usefixtures("make_dict_cred_for_new_user")
@pytest.mark.parametrize("name, email, password, roles, enable", [
    (name_admin_for_fixture, email_admin_for_fixture,
     test_password_for_fixture, roles_value_for_fixture, enable_value_for_fixture)
])
def test_create_user(name, email, password, roles, enable, make_dict_cred_for_new_user):
    url = url_user
    response = requests.post(url, make_dict_cred_for_new_user, verify=False)

    assert response.status_code != 200, "We can't create new device! "


@pytest.mark.skip
@pytest.mark.usefixtures("make_dict_cred_for_new_user")
@pytest.mark.parametrize("name, email, password, roles, enable", [
    (name_admin_for_fixture, email_admin_for_fixture,
     test_password_for_fixture, roles_value_for_fixture, enable_value_for_fixture)
])
def test_create_user_with_wrong_data(name, email, password, roles, enable, make_dict_cred_for_new_user):
    url = url_user
    response = requests.post(url, make_dict_cred_for_new_user, verify=False)

    assert response.status_code == 401, "Ups! We can't create new user with WRONG data!"


@pytest.mark.usefixtures("make_dict_cred_for_new_device")
@pytest.mark.parametrize("name, parent_id", [
    ("Sprinkler", "63bea125-46f1-4d59-b6ec-65000d13ac9f")
])
def test_create_devise(name, parent_id, make_dict_cred_for_new_device):
    url = url_devise
    response = requests.post(url, make_dict_cred_for_new_device, verify=False)

    assert response.status_code != 200, "We can't create new device! "


@pytest.mark.skip
@pytest.mark.usefixtures("make_dict_cred_for_new_device")
@pytest.mark.parametrize("device_id, device_name, device_type", [
    ("", "", ""),
    ("Python is strange programming language", "Python", ""),
    ("Python is strange programming language", "", "3.7"),
    ("", "Python", "3.7"),
    ("", "", "3.7"),
    ("Python is strange programming language", "", ""),
    ("", "Python", ""),
    ("Python is strange programming language", "Python", "3.7")
])
def test_create_devise_with_wrong_data(device_id, device_name, device_type, make_dict_cred_for_new_device):
    url = url_devise
    response = requests.post(url, make_dict_cred_for_new_device, verify=False)

    assert response.status_code == 401, "Ups! We can't create new device with WRONG data! "


@pytest.mark.usefixtures("make_dict_cred_for_new_service")
@pytest.mark.parametrize("test_comment, service_name", [
    ("Test Comment", "Sprinkler")
])
def test_create_service(test_comment, service_name, make_dict_cred_for_new_service):
    url = url_service
    response = requests.post(url, make_dict_cred_for_new_service, verify=False)

    assert response.status_code != 200, "We can't create new service!"


@pytest.mark.skip
@pytest.mark.usefixtures("make_dict_cred_for_new_service")
@pytest.mark.parametrize("test_comment, service_name", [
    ("", ""),
    ("Python is strange programming language", ""),
    ("", "Python")
])
def test_create_service_with_wrong_data(test_comment, service_name, make_dict_cred_for_new_service):
    url = url_service
    response = requests.post(url, make_dict_cred_for_new_service, verify=False)

    assert response.status_code == 401, "Ups! We can't create new service with WRONG data!"

# pytest --alluredir=/Users/alexandrvolchkov/Documents/Automation/APIsaas2/results
# allure serve /Users/alexandrvolchkov/Documents/Automation/APIsaas2/results
