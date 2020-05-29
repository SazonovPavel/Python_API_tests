# -*- coding: utf-8 -*-
import pytest
# from mysql_methods.methods_sql import clean_rt_in_mysql
from helpers.helpers import *
from data_for_test.data_rt_management import *

# Подключение сертификата безопасности SSL
# cafile = 'cacert.pem' # http://curl.haxx.se/ca/cacert.pem
# r = requests.get(url, verify=cafile)


@pytest.mark.usefixtures("get_new_jvt_token")
def test_create_new_section(get_new_jvt_token):
    id_uuid = get_id_uuid()
    id_uuid_for_section = get_id_uuid()

    create_draft_rt(get_new_jvt_token, id_uuid)
    response_json1 = send_request_get_rt_instance(get_new_jvt_token, id_uuid)
    number_before_add_section = get_number_of_sections(response_json1)
    assert number_before_add_section is None, "We have sections which we do not added!"

    send_request_create_section(get_new_jvt_token, make_data_for_new_section(id_uuid, id_uuid_for_section))

    response_json2 = send_request_get_rt_instance(get_new_jvt_token, id_uuid)
    number_after_add_section = get_number_of_sections(response_json2)
    assert len(number_after_add_section) == 1, "We have sections which we do not added!"


@pytest.mark.usefixtures("get_new_jvt_token")
def test_edit_section(get_new_jvt_token):
    id_uuid = get_id_uuid()
    id_uuid_for_section = get_id_uuid()

    create_draft_rt(get_new_jvt_token, id_uuid)
    response_json2 = send_request_get_rt_instance(get_new_jvt_token, id_uuid)
    number_before_add_section = get_number_of_sections(response_json2)
    assert number_before_add_section is None, "We have sections which we do not added!"

    send_request_create_section(get_new_jvt_token, make_data_for_new_section(id_uuid, id_uuid_for_section))

    send_request_edit_section(get_new_jvt_token, make_data_for_edit_section(id_uuid_for_section))

    response_json3 = send_request_get_rt_instance(get_new_jvt_token, id_uuid)
    edited_title = get_edited_section_title(response_json3)
    assert edited_title == "new_title", "We edit title but got wrong edited data!"


@pytest.mark.usefixtures("get_new_jvt_token")
def test_change_section_position(get_new_jvt_token):
    id_uuid = get_id_uuid()
    id_uuid_for_section1 = get_id_uuid()
    id_uuid_for_section2 = get_id_uuid()

    create_draft_rt(get_new_jvt_token, id_uuid)
    response_json2 = send_request_get_rt_instance(get_new_jvt_token, id_uuid)
    number_before_add_section = get_number_of_sections(response_json2)
    assert number_before_add_section is None, "We have sections which we do not added!"

    send_request_create_section(get_new_jvt_token, make_data_for_new_section(id_uuid, id_uuid_for_section1))

    send_request_create_section(get_new_jvt_token, make_data_for_second_section(id_uuid, id_uuid_for_section2))

    send_request_change_position_section(get_new_jvt_token,
                                         data_for_change_section_position_request(id_uuid_for_section2))

    response_json3 = send_request_get_rt_instance(get_new_jvt_token, id_uuid)
    section_position = get_section_position_by_number(response_json3, id_uuid_for_section2)
    assert section_position == 1, "We have sections which we do not added!"


@pytest.mark.usefixtures("get_new_jvt_token")
def test_delete_empty_section(get_new_jvt_token):
    id_uuid = get_id_uuid()
    id_uuid_for_section = get_id_uuid()

    create_draft_rt(get_new_jvt_token, id_uuid)
    send_request_create_section(get_new_jvt_token, make_data_for_new_section(id_uuid, id_uuid_for_section))

    response_json1 = send_request_get_rt_instance(get_new_jvt_token, id_uuid)
    number_before_deleting_section = get_number_of_sections(response_json1)
    assert len(number_before_deleting_section) == 1, "We have sections which we do not added!"

    send_request_delete_section(get_new_jvt_token, id_uuid_for_section)

    response_json2 = send_request_get_rt_instance(get_new_jvt_token, id_uuid)
    number_after_deleting_section = get_number_of_sections(response_json2)
    assert number_after_deleting_section is None, "We have sections which we do not added!"


@pytest.mark.usefixtures("get_new_jvt_token")
def test_delete_section_with_content(get_new_jvt_token):
    id_uuid = get_id_uuid()
    id_uuid_for_section = get_id_uuid()
    id_uuid_for_root_paragraph = get_id_uuid()

    create_draft_rt(get_new_jvt_token, id_uuid)
    send_request_create_section(get_new_jvt_token, make_data_for_new_section(id_uuid, id_uuid_for_section))
    send_request_create_root_paragraph_with_device(get_new_jvt_token,
                                                   make_data_for_new_root_paragraph_with_device(
                                                       id_uuid_for_root_paragraph,
                                                       id_uuid_for_section))

    response_json1 = send_request_get_rt_instance(get_new_jvt_token, id_uuid)
    number_before_deleting_section = get_number_of_sections(response_json1)
    assert len(number_before_deleting_section) == 1, "We have sections which we do not added!"

    send_request_delete_section(get_new_jvt_token, id_uuid_for_section)

    response_json2 = send_request_get_rt_instance(get_new_jvt_token, id_uuid)
    number_after_deleting_section = get_number_of_sections(response_json2)
    assert number_after_deleting_section == number_before_deleting_section, "We can delete section with content!"


# pytest --alluredir=/Users/alexandrvolchkov/Documents/Automation/APIsaas2/results
# pytest test_section_management.py --alluredir=/Users/alexandrvolchkov/Documents/Automation/APIsaas2/results
# allure serve /Users/alexandrvolchkov/Documents/Automation/APIsaas2/results
