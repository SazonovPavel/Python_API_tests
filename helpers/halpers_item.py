# -*- coding: utf-8 -*-
# используются
# import json
# from data_for_test.data_rt_management import *
import requests
from data_for_test.data_url_rt_section_paragraph import *


def send_request_create_input_item(get_new_jvt_token, data):
    url = url_input_item
    response = requests.post(url, json=data, headers=get_new_jvt_token)
    assert response.status_code == 201, "We can not create Input Item"


def send_request_create_list_item(get_new_jvt_token, data):
    url = url_list_item
    response = requests.post(url, json=data, headers=get_new_jvt_token)
    assert response.status_code == 201, "We can not create List Item"


def send_request_create_picture_item(get_new_jvt_token, data):
    url = url_picture_item
    response = requests.post(url, json=data, headers=get_new_jvt_token)
    assert response.status_code == 201, "We can not create Picture Item"


def send_request_create_device_information_item(get_new_jvt_token, data):
    url = url_device_information_item
    response = requests.post(url, json=data, headers=get_new_jvt_token)
    assert response.status_code == 201, "We can not create Device Information Item"


def send_request_edit_input_item(get_new_jvt_token, data):
    url = url_input_item
    response = requests.put(url, json=data, headers=get_new_jvt_token)
    assert response.status_code == 200, "We can not edit Input Item"


def send_request_edit_list_item(get_new_jvt_token, data):
    url = url_list_item
    response = requests.put(url, json=data, headers=get_new_jvt_token)
    assert response.status_code == 201, "We can not edit List Item"


def send_request_edit_picture_item(get_new_jvt_token, data):
    url = url_picture_item
    response = requests.put(url, json=data, headers=get_new_jvt_token)
    assert response.status_code == 200, "We can not edit Picture Item"


def send_request_edit_device_information_item(get_new_jvt_token, data):
    url = url_device_information_item
    response = requests.put(url, json=data, headers=get_new_jvt_token)
    assert response.status_code == 200, "We can not edit Picture Item"


def get_number_of_item(response_json):
    our_items = response_json["resultReportTemplate"]["sections"][0]["paragraphs"][0]["items"]
    assert our_items != 0, "We do not have any items!"
    return our_items


def get_answer_from_input_item(response_json):
    our_answer = \
        response_json["resultReportTemplate"]["sections"][0]["paragraphs"][0]["items"][0]["defaultAnswer"]["value"]
    return our_answer


def get_answer_from_list_item(response_json):
    our_answer = \
        response_json["resultReportTemplate"]["sections"][0]["paragraphs"][0]["items"][0]["defaultAnswer"]["id"]
    return our_answer


def get_label_from_picture_item(response_json):
    our_label = response_json["resultReportTemplate"]["sections"][0]["paragraphs"][0]["items"][0]["label"]
    return our_label


def get_label_from_device_information_item(response_json):
    our_label = response_json["resultReportTemplate"]["sections"][0]["paragraphs"][0]["items"][0]["label"]
    return our_label
