import pymysql


def clean_rt_in_mysql():
    connection = pymysql.connect(host="00.000.00.00",
                                 user="0000",
                                 password="0000",
                                 db="00")

    cursor = connection.cursor()

    print(cursor.execute("SHOW DATABASES"))
    # cursor.execute("DELETE  FROM ReportTemplates WERE id" + "=" + id_uuid)
    # а не запихнуть ли это к тестам чтоб не размазывать логику?
