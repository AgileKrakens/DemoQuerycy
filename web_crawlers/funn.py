from bs4 import BeautifulSoup
import requests

def cria_lista(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')

    span = soup.find_all('span')
    lista = [title.text.strip() for title in span]

    return(lista)



def acha_nome(lista):
    nome = 'Nome civil:'
    position = lista.index(nome)+1
    nome_vereador = lista[position]

    return(nome_vereador)


def acha_partido(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    span_partido = soup.find('span', id='partido')
    nome_partido = [title.text.strip() for title in span_partido]

    return(nome_partido)

def acha_telefone(lista):
    try:
        telefone = 'Telefone(s):'
        position = lista.index(telefone)+1
        num_telefone = lista[position]

        return(num_telefone)
    except:
        pass

def acha_celular(lista):

    cel = 'Celular:'
    position = lista.index(cel)+1
    celular = lista[position]

    return(celular)

def acha_email(lista):
    email = 'E-mail:'
    position = lista.index(email)+1
    email = lista[position]

    return(email)