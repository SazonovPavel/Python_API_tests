# -*- coding: utf-8 -*-
import json
import requests
from data_for_test.data_rt_management import *
from data_for_test.data_url_rt_section_paragraph import *


# Методы использующиеся в этом классе ибо дилема: либо тесты размером с мамонта,
# либо усложнение понимкния кода. Так что держитесь потомки(
def send_request_create_rt(data, get_new_jvt_token):
    url = url_post_create
    response = requests.post(url, json=data, headers=get_new_jvt_token, verify=False)
    assert response.status_code == 201, "We can't create new Report Template!"


def create_draft_rt(get_new_jvt_token, id_uuid):
    send_request_create_rt(make_data(id_uuid), get_new_jvt_token)
    response_json = send_request_get_rt_list(get_service_id(), get_new_jvt_token)
    status_rt_before_dell = get_param_from_response_json(response_json, id_uuid, "status")
    assert status_rt_before_dell == "draft", "We try delete not draft Report Template!"


def send_request_get_rt_list(need_id, get_new_jvt_token):
    url = url_get_list_by_service + "/" + need_id
    response = requests.get(url, headers=get_new_jvt_token)
    assert response.status_code == 200, "We can't got Report Template list by service_id!"
    response_json = json.loads(response.text)
    return response_json


def send_request_get_rt_instance(get_new_jvt_token, id_uuid):
    url = url_get_rt_by_id + "/" + id_uuid
    response = requests.get(url, headers=get_new_jvt_token)
    assert response.status_code == 200, "We can't find Report Template by UUid!"
    response_json = json.loads(response.text)
    return response_json


def send_request_delete_rt(get_new_jvt_token, id_uuid):
    url = url_delete + "/" + id_uuid
    response3 = requests.delete(url, headers=get_new_jvt_token, verify=False)
    assert response3.status_code == 204, "We can't delete Report Template by UUid!"


def send_request_archive_rt(get_new_jvt_token, id_uuid):
    url = url_put_archive + "/" + id_uuid
    response = requests.put(url, headers=get_new_jvt_token, verify=False)
    assert response.status_code == 200, "We can't archived Report Template by UUid!"


def send_request_publish_rt(get_new_jvt_token, id_uuid):
    url = url_put_publish + "/" + id_uuid
    response = requests.put(url, headers=get_new_jvt_token, verify=False)
    assert response.status_code == 200, "We can't publish Report Template by UUid!"


def send_request_duplicated(get_new_jvt_token, id_uuid):
    url = url_put_duplicate + "/" + id_uuid
    response = requests.post(url, headers=get_new_jvt_token, verify=False)
    assert response.status_code == 200, "We can't duplicate Report Template by UUid!"


def send_request_put(get_new_jvt_token, id_uuid):
    url = url_put_edit + "/" + id_uuid
    response = requests.put(url, json=make_put_data(), headers=get_new_jvt_token, verify=False)
    assert response.status_code == 200, "We can't edit Report Template by UUid!"


def send_request_create_section(get_new_jvt_token, data_for_section):
    url = url_create_section
    response = requests.post(url, json=data_for_section, headers=get_new_jvt_token, verify=False)
    assert response.status_code == 201, "We can't create new section!"


def send_request_delete_section(get_new_jvt_token, section_uuid):
    url = url_delete_section + "/" + section_uuid
    requests.delete(url, headers=get_new_jvt_token, verify=False)


def send_request_edit_section(get_new_jvt_token, data_for_edit_section):
    url = url_edit_section
    response = requests.put(url, json=data_for_edit_section, headers=get_new_jvt_token, verify=False)
    assert response.status_code == 200, "We can't edit section!"


def send_request_change_position_section(get_new_jvt_token, data_for_change_position):
    url = url_change_position_section
    response = requests.put(url, json=data_for_change_position, headers=get_new_jvt_token)
    assert response.status_code == 200, "We can't change section position!"


def send_request_create_root_paragraph_without_device(get_new_jvt_token, data):
    url = url_create_root_paragraph_without_device
    response = requests.post(url, json=data,
                             headers=get_new_jvt_token, verify=False)
    assert response.status_code == 201, "We can't create new root paragraph without device!"


def send_request_create_root_paragraph_with_device(get_new_jvt_token, data):
    url = url_create_root_paragraph_with_device
    response = requests.post(url, json=data,
                             headers=get_new_jvt_token, verify=False)
    assert response.status_code == 201, "We can't create new root paragraph with device!"


def send_request_create_child_paragraph_with_device(get_new_jvt_token, data):
    url = url_create_child_paragraph_with_device
    response = requests.post(url, json=data,
                             headers=get_new_jvt_token, verify=False)
    assert response.status_code == 201, "We can't create new child paragraph without device!"


def send_request_change_paragraph_position(get_new_jvt_token, data):
    url = url_change_position_paragraph
    response = requests.put(url, json=data, headers=get_new_jvt_token)
    assert response.status_code == 200, "We can't change section position!"


def send_request_edit_paragraph(get_new_jvt_token, id_for_root_paragraph_with_device, data):
    url = url_edit_paragraph + "/" + id_for_root_paragraph_with_device
    response = requests.put(url, json=data, headers=get_new_jvt_token)
    assert response.status_code == 200, "We can't change section position!"


def get_id_param_from_response_json(response_json, id_uuid, param):
    list_length = len(response_json["resultGetListByService"])
    assert list_length != 0, "List is EMPTY!"
    got_rt_param = ""

    i = 0
    while i <= list_length:
        got_rt_param = response_json["resultGetListByService"][i][param]
        if got_rt_param == id_uuid:
            break
        else:
            i = i + 1

    return got_rt_param


def get_param_from_response_json(response_json, id_uuid, param):
    list_length = len(response_json["resultGetListByService"])
    assert list_length != 0, "List is EMPTY!"

    get_status = ""

    i = 0
    while i <= list_length:
        got_rt_id = response_json["resultGetListByService"][i]["id"]
        if got_rt_id == id_uuid:
            get_status = response_json["resultGetListByService"][i][param]
            break
        else:
            i = i + 1

    return get_status


def get_duplicated_rt_description(response_json, id_uuid, description):
    list_length = len(response_json["resultGetListByService"])
    assert list_length != 0, "List is EMPTY!"

    get_dup_rt_id = ""

    i = 0
    while i <= list_length:
        got_rt_description = response_json["resultGetListByService"][i][description]
        if got_rt_description == id_uuid:
            get_id = response_json["resultGetListByService"][i]["id"]
            if get_id != id_uuid:
                get_dup_rt_id = get_id
                break
            else:
                i = i + 1
        else:
            i = i + 1

    return get_dup_rt_id


def get_number_of_sections(response_json):
    sections = response_json["resultReportTemplate"]["sections"]
    return sections


def get_edited_section_title(response_json):
    edited_title = response_json["resultReportTemplate"]["sections"][0]["title"]
    return edited_title


def get_section_position_by_number(response_json, id_uuid_for_section2):
    i_sections = len(response_json["resultReportTemplate"]["sections"])
    assert i_sections != 0, "We does not have sections"

    position_by_id = 0

    i = 0
    while i <= i_sections:
        current_section_id = response_json["resultReportTemplate"]["sections"][i]["id"]
        if current_section_id == id_uuid_for_section2:
            position_by_id = response_json["resultReportTemplate"]["sections"][i]["position"]
            break
        else:
            i = i + 1
    return position_by_id


def get_number_of_root_paragraph_in_section(response_json):
    number_of_paragraph = response_json["resultReportTemplate"]["sections"][0]["paragraphs"]
    assert number_of_paragraph != 0, "We no not have any paragraph!"
    return number_of_paragraph


def get_number_of_child_paragraph_in_section(response_json):
    number_of_paragraph = response_json["resultReportTemplate"]["sections"][0]["paragraphs"][0]["children"]
    assert number_of_paragraph != 0, "We no not have any paragraph!"
    return number_of_paragraph


def get_param_from_second_paragraph(response_json, id_uuid_second_paragraph, param):
    number_of_paragraph = len(response_json["resultReportTemplate"]["sections"][0]["paragraphs"])
    assert number_of_paragraph != 0, "We no not have any paragraph!"
    parameter = ""

    i = 0
    while i < number_of_paragraph:
        id_paragraph = response_json["resultReportTemplate"]["sections"][0]["paragraphs"][i]["id"]
        if id_paragraph == id_uuid_second_paragraph:
            parameter = response_json["resultReportTemplate"]["sections"][0]["paragraphs"][i][param]
            break
        else:
            i = i + 1
    return parameter


def get_param_of_paragraph_instance(response_json, param):
    number_of_paragraph = len(response_json["resultReportTemplate"]["sections"][0]["paragraphs"])
    assert number_of_paragraph != 0, "We no not have any paragraph!"
    return response_json["resultReportTemplate"]["sections"][0]["paragraphs"][0][param]


def get_device_list_for_root_paragraph_by_device_id(get_new_jvt_token, device_id):
    url = url_get_list_for_root_paragraph + device_id
    response = requests.post(url, headers=get_new_jvt_token, verify=False)
    assert response.status_code == 200, "We can't get list"
    response_json = response.json()
    return response_json


def get_list_for_child_paragraph_by_device_id(get_new_jvt_token, device_id):
    url = url_get_list_for_child_paragraph + device_id
    response = requests.post(url, headers=get_new_jvt_token, verify=False)
    assert response.status_code == 200, "We can't get list"
    response_json = response.json()
    return response_json
