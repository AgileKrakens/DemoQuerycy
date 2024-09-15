import info
import json
import re

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

url = input('\nurl do perfil do político: ')

dados_string = info.personal_data(url)

dados = {
    'nome': re.search(r'civil:(.*)', dados_string).group(1).strip(),
    'partido': info.partido(url),
    'telefone': re.findall(r'\(\d{2}\)\s\d{4}-\d{4}', dados_string),
    'email': re.search(r'E-mail:(.*)', dados_string).group(1).strip(),
    'mandatos': info.mandato(url)
}

#salva os dados em um JSON
with open('personal_data.json', 'w', encoding='utf-8') as json_file:
    json.dump(dados, json_file, ensure_ascii=False, indent=4)

print('\n\ndados coletados!')
                                                                                                                                                                                                    
                                                                                                                                                                                                    


