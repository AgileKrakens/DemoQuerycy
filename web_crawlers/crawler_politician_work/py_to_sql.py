import politician_work
import pymysql
import os
from datetime import datetime

base_dir = os.path.dirname(__file__)
urls_file = os.path.join(base_dir, "..", "crawler_personal_data", "camara_endpoints.txt")
data_list = politician_work.process_all_urls(urls_file)

connection = pymysql.connect(
        host='localhost',
        user='admin',
        password='qwerty',
        database='db',
        port=3306,
        ssl_disabled=True
    )

try:
    with connection.cursor() as cursor:
        for item in data_list:
            for key, value in item.items():
                tipo = value['Tipo']
                numero = int(value['Numero'])
                ano = int(value['Ano'])
                data = datetime.strptime(value['Data'], '%d/%m/%Y')
                autor = value['Autor']
                resumo = value['Resumo']
                situacao = value['Situacao']
                tema = value['Temas']

                sql = """
                INSERT INTO law_records (tipo, numero, ano, data, autor, resumo, situacao, tema)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(sql, (tipo, numero, ano, data, autor, resumo, situacao, tema))

        connection.commit()

finally:
    connection.close()
