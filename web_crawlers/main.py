import funn
from bs4 import BeautifulSoup
import requests

url_renato_santiago = 'https://camarasempapel.camarasjc.sp.gov.br/spl/parlamentar.aspx?id=245'
url_walter_hayashi = 'https://camarasempapel.camarasjc.sp.gov.br/spl/parlamentar.aspx?id=55'

lista = funn.cria_lista(url_renato_santiago)

nome_parlamentar = funn.acha_nome(lista)
partido = funn.acha_partido(url_renato_santiago)
telefone = funn.acha_telefone(lista)
cel = funn.acha_celular(lista)
email = funn.acha_email(lista)

print(nome_parlamentar)
print(partido)
print(telefone)
print(cel)
print(email)