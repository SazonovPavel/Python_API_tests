# main url
main_url = "https://1"
# main_url = "https://1"

# урлы используемые в тестом для работы с report template
url_post_create = main_url + "/api/v1/report-templates/create"
url_get_list_by_service = main_url + "/api/v1/report-templates/list-by-service"
url_get_rt_by_id = main_url + "/api/v1/report-templates"
url_delete = main_url + "/api/v1/report-templates/delete"
url_put_archive = main_url + "/api/v1/report-templates/archive"
url_put_publish = main_url + "/api/v1/report-templates/publish"
url_put_duplicate = main_url + "/api/v1/report-templates/duplicate"
url_put_edit = main_url + "/api/v1/report-templates/edit"

# урлы используемые в тестом для работы с section
url_create_section = main_url + "/api/v1/sections/create"
url_edit_section = main_url + "/api/v1/sections/edit"
url_change_position_section = main_url + "/api/v1/sections/change-position"
url_delete_section = main_url + "/api/v1/sections/delete"

# урлы используемые в тестом для работы с paragraph
url_create_root_paragraph_without_device = main_url + "/api/v1/paragraphs/create-root-without-device"
url_create_root_paragraph_with_device = main_url + "/api/v1/paragraphs/create-root-with-device"

url_create_child_paragraph_with_device = main_url + "/api/v1/paragraphs/create-child-with-device"

url_change_position_paragraph = main_url + "/api/v1/paragraphs/change-position"
url_edit_paragraph = main_url + "/api/v1/paragraphs/edit"

# урлы используемые в тестом для работы с device
url_get_list_for_root_paragraph = main_url + "/api/v1/devices/list-for-root-paragraph/"
url_get_list_for_child_paragraph = main_url + "/api/v1/devices/list-for-children-paragraph/"

# урлы используемые в тестом для работы с item
url_input_item = main_url + "/api/v1/items/input"
url_list_item = main_url + "/api/v1/items/list"
url_picture_item = main_url + "/api/v1/items/picture"
url_device_information_item = main_url + "/api/v1/items/device-information"
