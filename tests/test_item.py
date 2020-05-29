# -*- coding: utf-8 -*-
import pytest
# from mysql_methods.methods_sql import clean_rt_in_mysql
from helpers.halpers_item import *
from helpers.helpers import *
from data_for_test.data_rt_management import *

# Подключение сертификата безопасности SSL
# cafile = 'cacert.pem' # http://curl.haxx.se/ca/cacert.pem
# r = requests.get(url, verify=cafile)


# Short Text Input
@pytest.mark.usefixtures("get_new_jvt_token")
def test_create_input_item(get_new_jvt_token):
    id_uuid = get_id_uuid()
    id_uuid_for_section = get_id_uuid()
    id_uuid_for_root_paragraph = get_id_uuid()
    item_id = get_id_uuid()
    answer_id = get_id_uuid()

    create_draft_rt(get_new_jvt_token, id_uuid)

    send_request_create_section(get_new_jvt_token, make_data_for_new_section(id_uuid,
                                                                             id_uuid_for_section))

    send_request_create_root_paragraph_with_device(get_new_jvt_token,
                                                   make_data_for_new_root_paragraph_with_device(
                                                       id_uuid_for_root_paragraph,
                                                       id_uuid_for_section))
    data = make_data_for_create_input_item(item_id,
                                           id_uuid_for_root_paragraph,
                                           answer_id)

    send_request_create_input_item(get_new_jvt_token, data)

    response_json = send_request_get_rt_instance(get_new_jvt_token, id_uuid)
    number_item = get_number_of_item(response_json)
    assert len(number_item) == 1, "We have some wrong item number! Must be 1 item."


@pytest.mark.usefixtures("get_new_jvt_token")
def test_edit_input_item(get_new_jvt_token):
    id_uuid = get_id_uuid()
    id_uuid_for_section = get_id_uuid()
    id_uuid_for_root_paragraph = get_id_uuid()
    item_id = get_id_uuid()
    answer_id = get_id_uuid()

    create_draft_rt(get_new_jvt_token, id_uuid)

    send_request_create_section(get_new_jvt_token, make_data_for_new_section(id_uuid,
                                                                             id_uuid_for_section))

    send_request_create_root_paragraph_with_device(get_new_jvt_token,
                                                   make_data_for_new_root_paragraph_with_device(
                                                       id_uuid_for_root_paragraph,
                                                       id_uuid_for_section))
    data1 = make_data_for_create_input_item(item_id,
                                            id_uuid_for_root_paragraph,
                                            answer_id)

    send_request_create_input_item(get_new_jvt_token, data1)

    data2 = make_data_for_edit_input_item(item_id,
                                          id_uuid_for_root_paragraph,
                                          answer_id)

    send_request_edit_input_item(get_new_jvt_token, data2)

    response_json = send_request_get_rt_instance(get_new_jvt_token, id_uuid)
    edited_answer = get_answer_from_input_item(response_json)
    assert edited_answer == "Edited answer", "We got wrong edited answer!"


# Quick Select
@pytest.mark.usefixtures("get_new_jvt_token")
def test_create_list_item(get_new_jvt_token):
    id_uuid = get_id_uuid()
    id_uuid_for_section = get_id_uuid()
    id_uuid_for_root_paragraph = get_id_uuid()
    item_id = get_id_uuid()

    answer_id1 = get_id_uuid()
    answer_id2 = get_id_uuid()
    answer_id3 = get_id_uuid()

    create_draft_rt(get_new_jvt_token, id_uuid)

    send_request_create_section(get_new_jvt_token, make_data_for_new_section(id_uuid,
                                                                             id_uuid_for_section))

    send_request_create_root_paragraph_with_device(get_new_jvt_token,
                                                   make_data_for_new_root_paragraph_with_device(
                                                       id_uuid_for_root_paragraph,
                                                       id_uuid_for_section))
    data = make_data_for_create_list_item(item_id,
                                          id_uuid_for_root_paragraph,
                                          answer_id1,
                                          answer_id2,
                                          answer_id3)

    send_request_create_list_item(get_new_jvt_token, data)

    response_json = send_request_get_rt_instance(get_new_jvt_token, id_uuid)
    number_item = get_number_of_item(response_json)
    assert len(number_item) == 1, "We have some wrong item number! Must be 1 item."


# Quick Select
@pytest.mark.usefixtures("get_new_jvt_token")
def test_edit_list_item(get_new_jvt_token):
    id_uuid = get_id_uuid()
    id_uuid_for_section = get_id_uuid()
    id_uuid_for_root_paragraph = get_id_uuid()
    item_id = get_id_uuid()

    answer_id1 = get_id_uuid()
    answer_id2 = get_id_uuid()
    answer_id3 = get_id_uuid()

    create_draft_rt(get_new_jvt_token, id_uuid)

    send_request_create_section(get_new_jvt_token, make_data_for_new_section(id_uuid,
                                                                             id_uuid_for_section))

    send_request_create_root_paragraph_with_device(get_new_jvt_token,
                                                   make_data_for_new_root_paragraph_with_device(
                                                       id_uuid_for_root_paragraph,
                                                       id_uuid_for_section))
    data1 = make_data_for_create_list_item(item_id,
                                           id_uuid_for_root_paragraph,
                                           answer_id1,
                                           answer_id2,
                                           answer_id3)

    send_request_create_list_item(get_new_jvt_token, data1)

    response_json1 = send_request_get_rt_instance(get_new_jvt_token, id_uuid)
    default_answer_id = get_answer_from_list_item(response_json1)
    assert default_answer_id == answer_id1, "We got wrong answer!"

    data2 = make_data_for_edit_list_item(item_id,
                                         id_uuid_for_root_paragraph,
                                         answer_id1,
                                         answer_id2,
                                         answer_id3)

    send_request_edit_list_item(get_new_jvt_token, data2)

    response_json2 = send_request_get_rt_instance(get_new_jvt_token, id_uuid)
    edited_answer_id = get_answer_from_list_item(response_json2)
    assert edited_answer_id == answer_id3, "We got wrong edited answer!"


# Picture Item
@pytest.mark.usefixtures("get_new_jvt_token")
def test_create_picture_item(get_new_jvt_token):
    id_uuid = get_id_uuid()
    id_uuid_for_section = get_id_uuid()
    id_uuid_for_root_paragraph = get_id_uuid()
    item_id = get_id_uuid()

    create_draft_rt(get_new_jvt_token, id_uuid)

    send_request_create_section(get_new_jvt_token, make_data_for_new_section(id_uuid,
                                                                             id_uuid_for_section))

    send_request_create_root_paragraph_with_device(get_new_jvt_token,
                                                   make_data_for_new_root_paragraph_with_device(
                                                       id_uuid_for_root_paragraph,
                                                       id_uuid_for_section))
    data = make_data_for_create_picture_item(item_id,
                                             id_uuid_for_root_paragraph)

    send_request_create_picture_item(get_new_jvt_token, data)

    response_json = send_request_get_rt_instance(get_new_jvt_token, id_uuid)
    number_item = get_number_of_item(response_json)
    assert len(number_item) == 1, "We have some wrong item number! Must be 1 item."


@pytest.mark.usefixtures("get_new_jvt_token")
def test_edit_picture_item(get_new_jvt_token):
    id_uuid = get_id_uuid()
    id_uuid_for_section = get_id_uuid()
    id_uuid_for_root_paragraph = get_id_uuid()
    item_id = get_id_uuid()

    create_draft_rt(get_new_jvt_token, id_uuid)

    send_request_create_section(get_new_jvt_token, make_data_for_new_section(id_uuid,
                                                                             id_uuid_for_section))

    send_request_create_root_paragraph_with_device(get_new_jvt_token,
                                                   make_data_for_new_root_paragraph_with_device(
                                                       id_uuid_for_root_paragraph,
                                                       id_uuid_for_section))

    data_for_create = make_data_for_create_picture_item(item_id, id_uuid_for_root_paragraph)
    send_request_create_picture_item(get_new_jvt_token, data_for_create)

    response_json1 = send_request_get_rt_instance(get_new_jvt_token, id_uuid)
    default_label = get_label_from_picture_item(response_json1)
    assert default_label == "Label", "We got wrong edited answer!"

    data_for_edit = make_data_for_edit_picture_item(item_id, id_uuid_for_root_paragraph)
    send_request_edit_picture_item(get_new_jvt_token, data_for_edit)

    response_json2 = send_request_get_rt_instance(get_new_jvt_token, id_uuid)
    edited_label = get_label_from_picture_item(response_json2)
    assert edited_label == "Updated label", "We have some wrong item number! Must be 1 item."


# Написано на перед. На QA сервере пока не работает! 8-)
# Получаем 500 в методе send_request_get_rt_instance. Возможно из-за неготовых айтемов
@pytest.mark.usefixtures("get_new_jvt_token")
def test_create_device_information_item(get_new_jvt_token):
    id_uuid = get_id_uuid()
    id_uuid_for_section = get_id_uuid()
    id_uuid_for_root_paragraph = get_id_uuid()
    item_id = get_id_uuid()

    create_draft_rt(get_new_jvt_token, id_uuid)

    send_request_create_section(get_new_jvt_token, make_data_for_new_section(id_uuid,
                                                                             id_uuid_for_section))

    send_request_create_root_paragraph_with_device(get_new_jvt_token,
                                                   make_data_for_new_root_paragraph_with_device(
                                                       id_uuid_for_root_paragraph,
                                                       id_uuid_for_section))

    data_for_create = make_data_for_create_device_information_item(item_id, id_uuid_for_root_paragraph)
    send_request_create_device_information_item(get_new_jvt_token, data_for_create)

    response_json = send_request_get_rt_instance(get_new_jvt_token, id_uuid)
    number_item = get_number_of_item(response_json)
    assert len(number_item) == 1, "We have some wrong item number! Must be 1 item."


# Написано на перед. На QA сервере пока не работает! 8-)
# Получаем 500 в методе send_request_get_rt_instance. Возможно из-за неготовых айтемов
@pytest.mark.usefixtures("get_new_jvt_token")
def test_edit_device_information_item(get_new_jvt_token):
    id_uuid = get_id_uuid()
    id_uuid_for_section = get_id_uuid()
    id_uuid_for_root_paragraph = get_id_uuid()
    item_id = get_id_uuid()

    create_draft_rt(get_new_jvt_token, id_uuid)

    send_request_create_section(get_new_jvt_token, make_data_for_new_section(id_uuid,
                                                                             id_uuid_for_section))

    send_request_create_root_paragraph_with_device(get_new_jvt_token,
                                                   make_data_for_new_root_paragraph_with_device(
                                                       id_uuid_for_root_paragraph,
                                                       id_uuid_for_section))

    data_for_create = make_data_for_create_device_information_item(item_id, id_uuid_for_root_paragraph)
    send_request_create_device_information_item(get_new_jvt_token, data_for_create)

    response_json1 = send_request_get_rt_instance(get_new_jvt_token, id_uuid)
    default_label = get_label_from_device_information_item(response_json1)
    assert default_label == "Label", "We got wrong edited answer!"

    data_for_edit = make_data_for_edit_device_information_item(item_id, id_uuid_for_root_paragraph)
    send_request_edit_device_information_item(get_new_jvt_token, data_for_edit)

    response_json2 = send_request_get_rt_instance(get_new_jvt_token, id_uuid)
    edited_label = get_label_from_device_information_item(response_json2)
    assert edited_label == "Updated label", "We have some wrong item number! Must be 1 item."
