# -*- coding: utf-8 -*-
import pytest
# from mysql_methods.methods_sql import clean_rt_in_mysql
from helpers.helpers import *
from data_for_test.data_rt_management import *

# Подключение сертификата безопасности SSL
# cafile = 'cacert.pem' # http://curl.haxx.se/ca/cacert.pem
# r = requests.get(url, verify=cafile)


@pytest.mark.usefixtures("get_new_jvt_token")
def test_create_new_root_paragraph_without_devise(get_new_jvt_token):
    id_uuid = get_id_uuid()
    id_uuid_for_section1 = get_id_uuid()
    id_uuid_for_root_paragraph = get_id_uuid()

    create_draft_rt(get_new_jvt_token, id_uuid)

    send_request_create_section(get_new_jvt_token, make_data_for_new_section(id_uuid,
                                                                             id_uuid_for_section1))

    send_request_create_root_paragraph_without_device(get_new_jvt_token,
                                                      make_data_for_new_root_paragraph_without_device(
                                                          id_uuid_for_root_paragraph,
                                                          id_uuid_for_section1,
                                                          get_id_uuid_style_template()))

    response_json = send_request_get_rt_instance(get_new_jvt_token, id_uuid)
    number_of_paragraphs = get_number_of_root_paragraph_in_section(response_json)
    assert len(number_of_paragraphs) == 1, "We have paragraphs which we do not added!"


@pytest.mark.usefixtures("get_new_jvt_token")
def test_create_new_root_paragraph_with_devise(get_new_jvt_token):
    id_uuid = get_id_uuid()
    id_uuid_for_section1 = get_id_uuid()
    id_uuid_for_root_paragraph = get_id_uuid()

    create_draft_rt(get_new_jvt_token, id_uuid)

    send_request_create_section(get_new_jvt_token, make_data_for_new_section(id_uuid,
                                                                             id_uuid_for_section1))

    send_request_create_root_paragraph_with_device(get_new_jvt_token,
                                                   make_data_for_new_root_paragraph_with_device(
                                                          id_uuid_for_root_paragraph,
                                                          id_uuid_for_section1))

    response_json = send_request_get_rt_instance(get_new_jvt_token, id_uuid)
    number_of_paragraphs = get_number_of_root_paragraph_in_section(response_json)
    assert len(number_of_paragraphs) == 1, "We have paragraphs which we do not added!"


@pytest.mark.usefixtures("get_new_jvt_token")
def test_create_new_child_paragraph_with_device(get_new_jvt_token):
    id_uuid = get_id_uuid()
    id_uuid_for_section1 = get_id_uuid()
    id_uuid_for_root_paragraph = get_id_uuid()

    create_draft_rt(get_new_jvt_token, id_uuid)

    send_request_create_section(get_new_jvt_token, make_data_for_new_section(id_uuid,
                                                                             id_uuid_for_section1))

    send_request_create_root_paragraph_with_device(get_new_jvt_token,
                                                   make_data_for_new_root_paragraph_with_device(
                                                       id_uuid_for_root_paragraph,
                                                       id_uuid_for_section1))

    send_request_create_child_paragraph_with_device(get_new_jvt_token,
                                                    make_data_for_new_child_paragraph_with_device(
                                                        id_uuid, id_uuid_for_root_paragraph))

    response_json = send_request_get_rt_instance(get_new_jvt_token, id_uuid)
    number_of_paragraphs = get_number_of_child_paragraph_in_section(response_json)
    assert len(number_of_paragraphs) == 1, "We have paragraphs which we do not added!"


# @pytest.mark.usefixtures("get_new_jvt_token")
# @pytest.mark.parametrize("user_email, user_password, url_auth", [
#     (email_admin, test_password, url_auth_for_sign_in)
# ])
# def test_create_new_child_additional_paragraph(user_email, user_password, url_auth, get_new_jvt_token):
#     create_draft_rt(get_new_jvt_token)
#     send_request_create_section(get_new_jvt_token, make_data_for_new_section)


@pytest.mark.usefixtures("get_new_jvt_token")
def test_change_paragraph_position(get_new_jvt_token):
    id_uuid = get_id_uuid()
    id_uuid_for_section1 = get_id_uuid()
    id_uuid_for_root_paragraph = get_id_uuid()
    id_uuid_second_paragraph = get_id_uuid()

    create_draft_rt(get_new_jvt_token, id_uuid)

    send_request_create_section(get_new_jvt_token, make_data_for_new_section(id_uuid,
                                                                             id_uuid_for_section1))

    send_request_create_root_paragraph_with_device(get_new_jvt_token,
                                                   make_data_for_new_root_paragraph_with_device(
                                                       id_uuid_for_root_paragraph,
                                                       id_uuid_for_section1))

    send_request_create_root_paragraph_with_device(get_new_jvt_token,
                                                   make_data_for_new_root_paragraph_with_device_special(
                                                       id_uuid_second_paragraph,
                                                       id_uuid_for_section1))

    response_json1 = send_request_get_rt_instance(get_new_jvt_token, id_uuid)
    position_paragraph_before = get_param_from_second_paragraph(response_json1, id_uuid_second_paragraph, "position")
    assert position_paragraph_before == 2, "We don't have second paragraph!"

    send_request_change_paragraph_position(get_new_jvt_token,
                                           make_data_for_change_paragraph_position(id_uuid_second_paragraph))

    response_json2 = send_request_get_rt_instance(get_new_jvt_token, id_uuid)
    position_paragraph_after = get_param_from_second_paragraph(response_json2, id_uuid_second_paragraph, "position")
    assert position_paragraph_after == 1, "We don't have second paragraph!"


@pytest.mark.usefixtures("get_new_jvt_token")
def test_edit_paragraph(get_new_jvt_token):
    id_uuid = get_id_uuid()
    id_uuid_for_section1 = get_id_uuid()
    id_uuid_for_root_paragraph = get_id_uuid()

    create_draft_rt(get_new_jvt_token, id_uuid)

    send_request_create_section(get_new_jvt_token,
                                make_data_for_new_section(
                                    id_uuid,
                                    id_uuid_for_section1))

    send_request_create_root_paragraph_with_device(get_new_jvt_token,
                                                   make_data_for_new_root_paragraph_with_device(
                                                       id_uuid_for_root_paragraph,
                                                       id_uuid_for_section1))

    response_json1 = send_request_get_rt_instance(get_new_jvt_token, id_uuid)
    title_before_edit = get_param_of_paragraph_instance(response_json1, "headerValue")
    assert title_before_edit == "Paragraph Title", "We got wrong title! Check title in test data or refactor the test"

    send_request_edit_paragraph(get_new_jvt_token,
                                id_uuid_for_root_paragraph,
                                make_data_for_edit_paragraph())

    response_json2 = send_request_get_rt_instance(get_new_jvt_token, id_uuid)
    title_after_edit = get_param_of_paragraph_instance(response_json2, "headerValue")
    assert title_after_edit == "Edited Paragraph Title", "We can't edit title!"

# pytest --alluredir=/Users/alexandrvolchkov/Documents/Automation/APIsaas2/results
# pytest test_paragraph_management.py --alluredir=/Users/alexandrvolchkov/Documents/Automation/APIsaas2/results
# allure serve /Users/alexandrvolchkov/Documents/Automation/APIsaas2/results
