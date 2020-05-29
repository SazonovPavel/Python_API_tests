# -*- coding: utf-8 -*-
import pytest
# from mysql_methods.methods_sql import clean_rt_in_mysql
from helpers.helpers import *
from data_for_test.data_rt_management import *


# Подключение сертификата безопасности SSL
# cafile = 'cacert.pem' # http://curl.haxx.se/ca/cacert.pem
# r = requests.get(url, verify=cafile)


@pytest.mark.usefixtures("get_new_jvt_token")
def test_create_report_template(get_new_jvt_token):
    id_uuid = get_id_uuid()
    send_request_create_rt(make_data(id_uuid), get_new_jvt_token)
    response_json = send_request_get_rt_list(get_service_id(), get_new_jvt_token)
    got_rt_id = get_id_param_from_response_json(response_json, id_uuid, "id")
    assert got_rt_id == id_uuid, "Difference between sent and got deviceId!"


# перепроверить! Тест работал при упавшем сервере!!!=\
@pytest.mark.usefixtures("get_new_jvt_token")
def test_get_report_template_by_uuid(get_new_jvt_token):
    id_uuid = get_id_uuid()
    send_request_create_rt(make_data(id_uuid), get_new_jvt_token)

    rt_json = send_request_get_rt_instance(get_new_jvt_token, id_uuid)
    rt_id = rt_json["resultReportTemplate"]["id"]
    assert rt_id == id_uuid, "We can't find Report Template by UUid!"


# бага на сервере! Срабатывает метод 50/50 но тест ловит несрабатывание
# @pytest.mark.repeat(3)
@pytest.mark.usefixtures("get_new_jvt_token")
def test_get_report_template_list_by_service_id(get_new_jvt_token):
    url = url_get_list_by_service + "/" + get_service_id()
    response = requests.get(url, headers=get_new_jvt_token)
    assert response.status_code == 200, "We can't got Report Template list by service_id!"


@pytest.mark.usefixtures("get_new_jvt_token")
def test_delete_report_template_by_uuid(get_new_jvt_token):
    id_uuid = get_id_uuid()
    create_draft_rt(get_new_jvt_token, id_uuid)
    send_request_delete_rt(get_new_jvt_token, id_uuid)

    response_json = send_request_get_rt_list(get_service_id(), get_new_jvt_token)
    status_rt = get_param_from_response_json(response_json, id_uuid, "status")
    assert status_rt == "deleted", "Find test UUiD! We can't delete Report Template by UUid!"


@pytest.mark.usefixtures("get_new_jvt_token")
def test_archive_report_template_by_uuid(get_new_jvt_token):
    id_uuid = get_id_uuid()
    send_request_create_rt(make_data(id_uuid), get_new_jvt_token)
    send_request_publish_rt(get_new_jvt_token, id_uuid)

    response_json = send_request_get_rt_list(get_service_id(), get_new_jvt_token)
    status_rt_before_archiving = get_param_from_response_json(response_json, id_uuid, "status")
    assert status_rt_before_archiving == "published", "We try archive not published Report Template!"

    send_request_archive_rt(get_new_jvt_token, id_uuid)

    response_json2 = send_request_get_rt_list(get_service_id(), get_new_jvt_token)
    status_rt = get_param_from_response_json(response_json2, id_uuid, "status")
    assert status_rt == "archived", "Wrong status! We can't archive Report Template by UUid!"


@pytest.mark.usefixtures("get_new_jvt_token")
def test_publish_report_template_by_uuid(get_new_jvt_token):
    id_uuid = get_id_uuid()
    create_draft_rt(get_new_jvt_token, id_uuid)
    send_request_publish_rt(get_new_jvt_token, id_uuid)

    response_json = send_request_get_rt_list(get_service_id(), get_new_jvt_token)
    status_rt = get_param_from_response_json(response_json, id_uuid, "status")
    assert status_rt == "published", "Wrong status! We can't publish Report Template by UUid!"


@pytest.mark.usefixtures("get_new_jvt_token")
def test_re_publish_report_template_by_uuid(get_new_jvt_token):
    id_uuid = get_id_uuid()
    send_request_create_rt(make_data(id_uuid), get_new_jvt_token)
    send_request_archive_rt(get_new_jvt_token, id_uuid)
    response_json = send_request_get_rt_list(get_service_id(), get_new_jvt_token)
    status_rt_before_re_publish = get_param_from_response_json(response_json, id_uuid, "status")
    assert status_rt_before_re_publish == "archived", "We try publish not archived Report Template!"

    send_request_publish_rt(get_new_jvt_token, id_uuid)

    response_json = send_request_get_rt_list(get_service_id(), get_new_jvt_token)
    status_rt = get_param_from_response_json(response_json, id_uuid, "status")
    assert status_rt == "published", "Wrong status! We can't publish Report Template by UUid!"


@pytest.mark.usefixtures("get_new_jvt_token")
def test_duplicate_draft_report_template_by_uuid(get_new_jvt_token):
    id_uuid = get_id_uuid()
    send_request_create_rt(make_data_for_duplicate(id_uuid), get_new_jvt_token)
    response_json = send_request_get_rt_list(get_service_id(), get_new_jvt_token)
    status_rt_before_duplicated = get_param_from_response_json(response_json, id_uuid, "status")
    assert status_rt_before_duplicated == "draft", "We try duplicate not draft Report Template!"

    send_request_duplicated(get_new_jvt_token, id_uuid)

    response_json = send_request_get_rt_list(get_service_id(), get_new_jvt_token)
    get_dup_rt_id = get_duplicated_rt_description(response_json, id_uuid, "description")
    assert get_dup_rt_id != id_uuid, "We can't duplicate Report Template by UUid!"


@pytest.mark.usefixtures("get_new_jvt_token")
def test_duplicate_published_report_template_by_uuid(get_new_jvt_token):
    id_uuid = get_id_uuid()
    send_request_create_rt(make_data_for_duplicate(id_uuid), get_new_jvt_token)
    send_request_publish_rt(get_new_jvt_token, id_uuid)
    response_json = send_request_get_rt_list(get_service_id(), get_new_jvt_token)
    status_rt_before_duplicated = get_param_from_response_json(response_json, id_uuid, "status")
    assert status_rt_before_duplicated == "published", "We try duplicate not draft Report Template!"

    send_request_duplicated(get_new_jvt_token, id_uuid)

    response_json = send_request_get_rt_list(get_service_id(), get_new_jvt_token)
    get_dup_rt_id = get_duplicated_rt_description(response_json, id_uuid, "description")
    assert get_dup_rt_id != id_uuid, "We can't duplicate Report Template by UUid!"


@pytest.mark.usefixtures("get_new_jvt_token")
def test_duplicate_archived_report_template_by_uuid(get_new_jvt_token):
    id_uuid = get_id_uuid()
    send_request_create_rt(make_data_for_duplicate(id_uuid), get_new_jvt_token)
    send_request_publish_rt(get_new_jvt_token, id_uuid)
    send_request_archive_rt(get_new_jvt_token, id_uuid)
    response_json = send_request_get_rt_list(get_service_id(), get_new_jvt_token)
    status_rt_before_duplicated = get_param_from_response_json(response_json, id_uuid, "status")
    assert status_rt_before_duplicated == "archived", "We try duplicate not draft Report Template!"

    send_request_duplicated(get_new_jvt_token, id_uuid)

    response_json = send_request_get_rt_list(get_service_id(), get_new_jvt_token)
    get_dup_rt_id = get_duplicated_rt_description(response_json, id_uuid, "description")
    assert get_dup_rt_id != id_uuid, "We can't duplicate Report Template by UUid!"


@pytest.mark.usefixtures("get_new_jvt_token")
def test_edit_report_template_by_uuid(get_new_jvt_token):
    id_uuid = get_id_uuid()
    create_draft_rt(get_new_jvt_token, id_uuid)
    send_request_put(get_new_jvt_token, id_uuid)

    response_json2 = send_request_get_rt_list(get_service_id(), get_new_jvt_token)
    get_edited_description = get_param_from_response_json(response_json2, id_uuid, "description")
    get_edited_name = get_param_from_response_json(response_json2, id_uuid, "name")
    assert get_edited_description == "Test", "We can't edit Report Template by UUid!"
    assert get_edited_name == "Backflow Inspection", "We can't edit Report Template by UUid!"


# pytest --alluredir=/Users/alexandrvolchkov/Documents/Automation/APIsaas2/results

# pytest test_report_template_management.py --alluredir=/Users/alexandrvolchkov/
# Documents/Automation/APIsaas2/results

# allure serve /Users/alexandrvolchkov/Documents/Automation/APIsaas2/results
