import requests
import time

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
