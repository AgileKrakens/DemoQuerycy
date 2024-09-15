from bs4 import BeautifulSoup
import requests
import re

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

def mandato(url):
    div_mandatos = http_get(url).find('div', class_='kt-timeline-v1__item-content')
    return div_mandatos.text
