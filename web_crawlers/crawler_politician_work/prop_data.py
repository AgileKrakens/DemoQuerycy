import requests
import time
import pymysql
from datetime import datetime

class PublicRecord:
    def __init__(self, processo, ano, tipo, assunto, data, situacao, arquivo, autor):
        self.processo = processo
        self.ano = ano
        self.tipo = tipo
        self.assunto = assunto
        self.data = self.parse_date(data) 
        self.situacao = situacao
        self.arquivo = arquivo
        self.autor = autor

    @staticmethod
    def parse_date(data):
        return datetime.strptime(data, "%d/%m/%Y %H:%M:%S") if data else None

def save_to_mysql(records):
    connection = pymysql.connect(
        host='localhost',
        user='admin',
        password='qwerty',
        database='db',
        port=3306,
        ssl_disabled=True
    )
    cursor = connection.cursor()
    
    for record in records:
        sql = """
        INSERT INTO public_records (processo, ano, tipo, assunto, data, situacao, arquivo, autor)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            processo = VALUES(processo),
            ano = VALUES(ano),
            tipo = VALUES(tipo),
            assunto = VALUES(assunto),
            data = VALUES(data),
            situacao = VALUES(situacao),
            arquivo = VALUES(arquivo),
            autor = VALUES(autor);
        """
        cursor.execute(sql,
            (
                record.processo,
                record.ano,
                record.tipo,
                record.assunto,
                record.data,
                record.situacao,
                record.arquivo,
                record.autor
            )
        )
        
    connection.commit()
    cursor.close()
    connection.close()

def fetch_data(url, autor_ids, anos):
    records = []
    
    for autor_id in autor_ids:
        for ano in anos:
            endpoint = f"{url}?autorID={autor_id}&ano={ano}"
            response = requests.get(endpoint)
            
            if response.status_code == 200:
                json_data = response.json()
                for item in json_data.get('Data', []):
                    record = PublicRecord(
                        processo= item.get('processo'),
                        ano= item.get('ano'),
                        tipo=item.get('tipo'),
                        assunto=item.get('assunto'),
                        data=item.get('data'),
                        situacao=item.get('situacao'),
                        arquivo=item.get('arquivo'),
                        autor = item.get('AutorRequerenteDados', {}).get('nomeRazao')
                    )
                    records.append(record)
                print(f"Dados coletados em {endpoint}")
            else:
                print(f"Erro na requisição do endpoint: {endpoint}")
                
            # sleep para evitar DoS na API
            time.sleep(1)
    
    return records

def main():
    url = 'https://camarasempapel.camarasjc.sp.gov.br/api/publico/proposicao/'
    autor_ids = [1137, 1140, 1141, 1144, 1145, 1148, 1151, 1152, 1156, 1160, 1274, 3702, 3703, 3704, 3705, 3706, 3707, 3708, 3709, 3710, 4140]
    anos = [2020, 2021, 2022, 2023, 2024]
    
    records = fetch_data(url, autor_ids, anos)
    save_to_mysql(records)
    return 'sucess insert'

main()

