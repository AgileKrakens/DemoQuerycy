import requests
import time

url = 'https://camarasempapel.camarasjc.sp.gov.br//api/publico/proposicao/'
autor_ids = [1137,1140,1141,1144,1145,1148,1151,1152,1156,1160,1274,3702,3703,3704,3705,3706,3707,3708,3709,3710,4140]
anos = [2020,2021,2022,2023,2024]

def fetch_data(url, autor_ids, anos):
    data_collected = []
    
    for autor_id in autor_ids:
        for ano in anos:
            endpoint = f"{url}?autorID={autor_id}&ano={ano}"
            response = requests.get(endpoint)
            
            if response.status_code == 200:
                json_data = response.json()
                for item in json_data.get('Data', []):
                    data = {
                        'processo': item.get('processo'),
                        'ano': item.get('ano'),
                        'tipo': item.get('tipo'),
                        'assunto': item.get('assunto'),
                        'data': item.get('data'),
                        'situacao': item.get('situacao'),
                        'arquivo': item.get('arquivo'),
                        'autor': item.get('AutorRequerenteDados', {}).get('nomeRazao')
                    }
                    data_collected.append(data)
                print(f"Dados coletados em {endpoint}")
            else:
                print(f"Erro na requisição do endpoint: {endpoint}")
                
            time.sleep(1)
            
    return data_collected
    
print(fetch_data(url,autor_ids,anos))
