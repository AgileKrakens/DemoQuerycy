import sys
import json
import re
import info_camara
import info_tse

print('''

 
 
▓█████▄▓█████ ███▄ ▄███▓▒█████   █████  █    ██▓█████ ██▀███▓██   ██▓▄████▓██   ██▓
▒██▀ ██▓█   ▀▓██▒▀█▀ ██▒██▒  ██▒██▓  ██▒██  ▓██▓█   ▀▓██ ▒ ██▒██  ██▒██▀ ▀█▒██  ██▒
░██   █▒███  ▓██    ▓██▒██░  ██▒██▒  ██▓██  ▒██▒███  ▓██ ░▄█ ▒▒██ ██▒▓█    ▄▒██ ██░             
░▓█▄   ▒▓█  ▄▒██    ▒██▒██   ██░██  █▀ ▓▓█  ░██▒▓█  ▄▒██▀▀█▄  ░ ▐██▓▒▓▓▄ ▄██░ ▐██▓░     
░▒████▓░▒████▒██▒   ░██░ ████▓▒░▒███▒█▄▒▒█████▓░▒████░██▓ ▒██▒░ ██▒▓▒ ▓███▀ ░ ██▒▓░
 ▒▒▓  ▒░░ ▒░ ░ ▒░   ░  ░ ▒░▒░▒░░░ ▒▒░ ▒░▒▓▒ ▒ ▒░░ ▒░ ░ ▒▓ ░▒▓░ ██▒▒▒░ ░▒ ▒  ░██▒▒▒ 
 ░ ▒  ▒ ░ ░  ░  ░      ░ ░ ▒ ▒░ ░ ▒░  ░░░▒░ ░ ░ ░ ░  ░ ░▒ ░ ▒▓██ ░▒░  ░  ▒ ▓██ ░▒░ 
 ░ ░  ░   ░  ░      ░  ░ ░ ░ ▒    ░   ░ ░░░ ░ ░   ░    ░░   ░▒ ▒ ░░ ░      ▒ ▒ ░░  
   ░      ░  ░      ░      ░ ░     ░      ░       ░  ░  ░    ░ ░    ░ ░    ░ ░     
 ░                                                           ░ ░    ░      ░ ░     


                            your digital democracy is running by
                                     --Agile Krakens                                         
''')

def scrap(url, url2):
    dados_string = info.personal_data(url)
    dados_presenca = info.presence_stats(url)
    comissoes = info.comissoes(url)
    
    dados = {
        'nome': re.search(r'civil:(.*)', dados_string).group(1).strip(),
        'nome_social':
        'data_nasc':
        'ocupação': 
        'partido': info.partido(url)
        'telefone': re.findall(r'\(\d{2}\)\s\d{4}-\d{4}', dados_string),
        'email': re.search(r'E-mail:(.*)', dados_string).group(1).strip() if re.search(r'E-mail:(.*)', dados_string) else '',
        'comissoes': re.findall(r'Cargo: (.*?) \((.*?)\)\nComissão: (.*?)-'
        'presencas': [x for x in dados_presenca[:dados_presenca.index('Falta')] if x.isdigit()]
        'ausencias': [x for x in dados_presenca[dados_presenca.index('Falta'):] if x.isdigit()]
        'mandatos': 
    }

    file = f"{dados['nome'].replace(' ', '_').lower()}.json"
    
    with open(f"/home/kali/Desktop/DemoQuerycy/src/data/vereadores/{file}", 'w', encoding='utf-8') as json_file:
        json.dump(dados, json_file, ensure_ascii=False, indent=4)
        
    print(f"\n{dados['nome']} data collected!")
    print(dados)

def read_urls(): #Incluir url2 no loop
    urls = sys.stdin.read().splitlines()
    
    for url in urls:
        try:
            scrap(url)
        except Exception as e:
            print(f"fail to process {url}: {e}")

read_urls()
