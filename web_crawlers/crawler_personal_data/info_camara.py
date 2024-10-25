from bs4 import BeautifulSoup
import requests

def http_get(url):
    response = requests.get(url)
    html = BeautifulSoup(response.text, 'html.parser')
    return html
    
def personal_data(url):
    div_dados = http_get(url).find(id='dados_parlamentar')
    return div_dados.text

def partido(url):
    div_partido = http_get(url).find(id='partido')
    return div_partido.text

def comissoes(url):
    div_mandatos = http_get(url).find('div', class_='kt-timeline-v1__item-content')
    return div_mandatos.text
       
def presence_stats(url):
    url = url + '#tab_frequencia_plenario'
    div_presence = http_get(url).find(id='tab_frequencia_plenario')
    return div_presence.text.split()


