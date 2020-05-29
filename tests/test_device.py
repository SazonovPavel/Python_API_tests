# -*- coding: utf-8 -*-
import pytest
# from mysql_methods.methods_sql import clean_rt_in_mysql
from helpers.helpers import *
from data_for_test.data_rt_management import *

# Подключение сертификата безопасности SSL
# cafile = 'cacert.pem' # http://curl.haxx.se/ca/cacert.pem
# r = requests.get(url, verify=cafile)


@pytest.mark.usefixtures("get_new_jvt_token")
def test_get_list_for_root_paragraph_by_device_id(get_new_jvt_token):
    device_id = get_id_uuid_device_sprinkler()
    got_json = get_device_list_for_root_paragraph_by_device_id(get_new_jvt_token, device_id)

    filter_one = got_json["getDeviceGroupsResponse"][0]["filter"]["name"]
    filter_two = got_json["getDeviceGroupsResponse"][1]["filter"]["name"]

    assert filter_one == "Related to an inspected device",\
        "We got wrong name of filter for related tu an inspected device"
    assert filter_two == "Every on site", \
        "We got wrong name of filter for every on site device"


@pytest.mark.usefixtures("get_new_jvt_token")
def test_get_list_for_child_paragraph_by_device_id(get_new_jvt_token):
    device_id = get_id_uuid_device_facp()
    got_json = get_list_for_child_paragraph_by_device_id(get_new_jvt_token, device_id)

    filter_one = got_json["getDeviceGroupsResponse"][0]["name"]

    assert filter_one == "Related to inspected device", \
        "We got wrong name of filter for related tu an inspected device"


# pytest --alluredir=/Users/alexandrvolchkov/Documents/Automation/APIsaas2/results
# pytest test_device.py --alluredir=/Users/alexandrvolchkov/Documents/Automation/APIsaas2/results
# allure serve /Users/alexandrvolchkov/Documents/Automation/APIsaas2/results
