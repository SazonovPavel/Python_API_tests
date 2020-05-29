# -*- coding: utf-8 -*-
import uuid


# Переменные для создания темплейтов статические - строки
def specific_template_uuid():
    specific_id = "63bea125-46f1-4d59-b6ec-65000d13ac23"
    return specific_id


# А вот тут uuid для РАЗНЫХ девайсов
def get_id_uuid_device_sprinkler():
    device_id = "63bea125-46f1-4d59-b6ec-65000d13ac1f"
    return device_id


def get_id_uuid_device_facp():
    device_id = "0456cf66-177f-4186-8978-d332102b31ff"
    return device_id


def get_id_uuid_second_paragraph():
    second_par_id = "7d3c5ce3-fa09-4632-95ab-aeb231d6ca76"
    return second_par_id


# def id_uuid_filter():
# return str(uuid.uuid4())
def get_filter_on_site():
    filter1 = "on_site"
    return filter1


# def id_uuid_style_template():
# return str(uuid.uuid4())
def get_id_uuid_style_template():
    style = "c11bbcc0-7862-4ffa-8669-586bca31e4c6"
    return style


def get_service_id():
    service_id = "63bea125-46f1-4d59-b6ec-65000d13acc1"
    return service_id


def get_id_uuid():
    return str(uuid.uuid4())


def make_data(id_uuid):
    data = {
        "createReportTemplateRequest":
            {
                "id": id_uuid,
                "deviceId": "63bea125-46f1-4d59-b6ec-65000d13ac1f",
                "serviceId": "63bea125-46f1-4d59-b6ec-65000d13acc1",
                "name": "Test",
                "description": "Fire Alarm System description"
            }
    }
    return data


def make_put_data():
    data = {
        "editReportTemplateRequest":
            {
                "name": "Backflow Inspection",
                "description": "Test"
            }
    }
    return data


def make_data_for_duplicate(id_uuid):
    data = {
        "createReportTemplateRequest":
            {
                "id": id_uuid,
                "deviceId": "63bea125-46f1-4d59-b6ec-65000d13ac1f",
                "serviceId": "63bea125-46f1-4d59-b6ec-65000d13acc1",
                "name": "Test",
                "description": id_uuid
            }
    }
    return data


def make_data_for_new_section(id_uuid, id_for_section_one):
    data = {
        "createSectionRequest":
            {
                "reportTemplateId": id_uuid,
                "sectionId": id_for_section_one,
                "title": "Fire Inspection Title"
            }
    }
    return data


def make_data_for_second_section(id_uuid, id_for_section_two):
    data = {
        "createSectionRequest":
            {
                # какие поля должны быть динамическими и какие захардкодить?
                # какие должны быть отправлены данные для создания секци?
                "reportTemplateId": id_uuid,
                "sectionId": id_for_section_two,
                "title": "Second section must be first!"
            }
    }
    return data


def make_data_for_edit_section(id_for_section_one):
    data = {
        "editSectionRequest": {
            "id": id_for_section_one,
            "title": "new_title"
        }
    }
    return data


def data_for_change_section_position_request(id_for_section2):
    data = {
        "changeSectionPositionRequest": {
            # id секции для теста увеличено на 1 от стандартного
            "id": id_for_section2,
            "newPosition": "1"
        }
    }
    return data


def make_data_for_new_root_paragraph_without_device(id_uuid_for_root_paragraph,
                                                    id_uuid_for_section1,
                                                    id_uuid_style_template):
    data = {
        "createParagraphRequest":
            {
                "id": id_uuid_for_root_paragraph,
                "sectionId": id_uuid_for_section1,
                "title": "Paragraph Title",
                "styleTemplateId": id_uuid_style_template
            }
    }
    return data


def make_data_for_new_root_paragraph_with_device(id_uuid_for_root_paragraph,
                                                 id_uuid_for_section1):
    data = {
        "createParagraphRequest":
            {
                "id": id_uuid_for_root_paragraph,
                "sectionId": id_uuid_for_section1,
                "title": "Paragraph Title",
                "deviceId": get_id_uuid_device_sprinkler(),
                "filterId": get_filter_on_site(),
                "styleTemplateId": get_id_uuid_style_template()
            }
    }
    return data


def make_data_for_new_root_paragraph_with_device_special(id_second_paragraph,
                                                         id_for_section_one):
    data = {
        "createParagraphRequest":
            {
                "id": id_second_paragraph,
                "sectionId": id_for_section_one,
                "title": "Paragraph Title",
                "deviceId": get_id_uuid_device_sprinkler(),
                "filterId": get_filter_on_site(),
                "styleTemplateId": get_id_uuid_style_template()
            }
    }
    return data


def make_data_for_new_child_paragraph_with_device(id_for_child_paragraph_with_device,
                                                  id_for_root_paragraph_with_device):
    data = {
        "createParagraphRequest":
            {
                "id": id_for_child_paragraph_with_device,
                "parentId": id_for_root_paragraph_with_device,
                "title": "Child Paragraph Title",
                "deviceId": get_id_uuid_device_sprinkler(),
                "filterId": get_filter_on_site(),
                "styleTemplateId": get_id_uuid_style_template()
            }
    }
    return data


def make_data_for_change_paragraph_position(id_uuid_second_paragraph):
    data = {
        "changeParagraphPositionRequest":
            {
                "id": id_uuid_second_paragraph,
                "newPosition": "1"
            }
    }
    return data


def make_data_for_edit_paragraph():
    data = {
        "editParagraphRequest":
            {
                "title": "Edited Paragraph Title"
            }
    }
    return data


def make_data_for_create_input_item(item_id, paragraph_id, answer_id):
    data = {
        "createInputItem":
            {
                "id": item_id,
                "paragraphId": paragraph_id,
                "label": "test",
                "itemTypeId": "short_text_input",
                "defaultAnswer": {
                    "answerId": answer_id,
                    "value": "Some default answer",
                    "answerAssessment": "none"
                },
                "placeholder": "test",
                "NFPAref": "1",
                "required": False,
                "remembered": True
            }
    }
    return data


def make_data_for_edit_input_item(item_id, paragraph_id, answer_id):
    data = {
        "updateInputItem":
            {
                "id": item_id,
                "paragraphId": paragraph_id,
                "label": "updated",
                "itemTypeId": "short_text_input",
                "defaultAnswer": {
                    "answerId": answer_id,
                    "value": "Edited answer",
                    "answerAssessment": "none"
                },
                "placeholder": "test",
                "NFPAref": "1",
                "required": False,
                "remembered": True
            }
    }
    return data


def make_data_for_create_list_item(item_id, paragraph_id, answer_id1, answer_id2, answer_id3):
    data = {
        "createListItem": {
            "id": item_id,
            "paragraphId": paragraph_id,
            "label": "test",
            "itemTypeId": "quick_select",
            "answers": [
                {
                    "answerId": answer_id1,
                    "value": "Some default answer",
                    "answerAssessment": "none"
                },
                {
                    "answerId": answer_id2,
                    "value": "Some answer 1",
                    "answerAssessment": "none"
                },
                {
                    "answerId": answer_id3,
                    "value": "Some answer 2",
                    "answerAssessment": "negative"
                }
            ],
            "defaultAnswer": {
                "answerId": answer_id1
            },
            "placeholder": "test",
            "NFPAref": "1",
            "required": False,
            "remembered": True,
            "printable": True
        }
    }
    return data


def make_data_for_edit_list_item(item_id, paragraph_id, answer_id1, answer_id2, answer_id3):
    data = {
        "updateListItem": {
            "id": item_id,
            "paragraphId": paragraph_id,
            "label": "updated test",
            "itemTypeId": "quick_select",
            "answers": [
                {
                    "answerId": answer_id1,
                    "value": "Some default answer"
                },
                {
                    "answerId": answer_id2,
                    "value": "Some answer 1"
                },
                {
                    "answerId": answer_id3,
                    "value": "Some answer 2"
                }
            ],
            "defaultAnswer": {
                "answerId": answer_id3
            },
            "placeholder": "updated test",
            "NFPAref": "lolll",
            "required": False,
            "remembered": True
        }
    }
    return data


def make_data_for_create_picture_item(item_id, paragraph_id):
    data = {
        "createPictureItem": {
            "id": item_id,
            "paragraphId": paragraph_id,
            "itemTypeId": "photo",
            "label": "Label",
            "NFPAref": "1",
            "required": False,
            "remembered": True,
            "printable": True
        }
    }
    return data


def make_data_for_edit_picture_item(item_id, paragraph_id):
    data = {
        "updatePictureItem": {
            "id": item_id,
            "paragraphId": paragraph_id,
            "itemTypeId": "photo",
            "label": "Updated label",
            "NFPAref": "1",
            "required": False,
            "remembered": True,
            "printable": True
        }
    }
    return data


def make_data_for_create_device_information_item(item_id, id_uuid_for_root_paragraph):
    data = {
        "createDeviceInformationItem": {
            "id": item_id,
            "paragraphId": id_uuid_for_root_paragraph,
            "label": "Label",
            "itemTypeId": "information_device_related",
            "infoSource": {
                "infoSourceId": "backflow_size"
            },
            "printable": True
        }
    }
    return data


def make_data_for_edit_device_information_item(item_id, id_uuid_for_root_paragraph):
    data = {
        "createDeviceInformationItem": {
            "id": item_id,
            "paragraphId": id_uuid_for_root_paragraph,
            "label": "Updated label",
            "itemTypeId": "information_device_related",
            "infoSource": {
                "infoSourceId": "backflow_make"
            },
            "printable": True
        }
    }
    return data
