import requests
import time

url = 'https://camarasempapel.camarasjc.sp.gov.br//api/publico/proposicao/'
autor_ids = [1137,1140,1141,1144,1145,1148,1151,1152,1156,1160,1274,3702,3703,3704,3705,3706,3707,3708,3709,3710,4140]
anos = [2020,2021,2022,2023,2024]

def request_endp(url, autor_ids, anos):
    data = {}
    
    for autor_id in autor_ids:
        data[autor_id] = {}
        
        for ano in anos:
            endpoint = f"{url}?autorID={autor_id}&ano={ano}"
            
            response = requests.get(endpoint)
            
            if response.status_code == 200:
                data[autor_id][ano] = response.json()
                print(f"Dados coletados em {url}")
            else:
                print(f"Erro na requisição do endpoint: {url}")
                
            time.sleep(1)
            
    return data
    
print(request_endp(url,autor_ids,anos))
