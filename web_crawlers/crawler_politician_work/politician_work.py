import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

# Caminho relativo para o arquivo de URLs a partir de politician_work.py
base_dir = os.path.dirname(__file__)  # Diretório onde politician_work.py está localizado
urls_file = os.path.join(base_dir, "..", "crawler_personal_data", "camara_endpoints.txt")


def read_urls(urls_file):
    with open(urls_file, 'r') as f:
        urls = f.read().splitlines()
    return urls

def get_LA(url):
    service = Service()

    options = webdriver.ChromeOptions()
    # options.add_argument("--headless=new")  # Descomente para rodar em modo headless
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)
    time.sleep(2)

    leis_de_autoria = driver.find_element(By.XPATH, '//*[@id="link_leis_autoria"]/a')
    leis_de_autoria.click()
    time.sleep(2)
    
    limite = 0
    for xpath in range(1, 6):  # Altere para 6 para cobrir todos os elementos
        try:
            driver.find_element(By.XPATH, f'//*[@id="tab_leis_autoria"]/div/div[{xpath}]/div[1]/div/a')
            limite += 1
        except NoSuchElementException:
            continue

    dicionario = {}  # Declara o dicionário antes do loop para coletar dados de todas as páginas
    colunas = ['Tipo', 'Numero', 'Ano', 'Data', 'Origem',  'Autor', 'Resumo', 'Situacao', 'Temas']
    
    for i in range(1, limite + 1):
        la = driver.find_element(By.XPATH, f'//*[@id="tab_leis_autoria"]/div/div[{i}]/div[1]/div/a')
        la.click()
        time.sleep(2)

        press = driver.find_element(By.XPATH, '//*[@id="btn_impressao"]')
        press.click()

        qtd = int(driver.find_element(By.XPATH, '//*[@id="total"]/h1[1]/strong').text)
        
        for k in range(1, qtd + 1):
            dado = {}
            codigo = None
            for x in range(1, 10):
                if x == 5:
                    continue

                if x == 6:
                    info = driver.find_element(By.XPATH, '//*[@id="filtros"]/span[2]/strong')
                    dado["Autor"] = info.text  # Nomeie a coluna com a chave correta
                else:
                    info = driver.find_element(By.XPATH, f'//*[@id="relatorio"]/tr[{k}]/td[{x}]')

                # Construindo o código (usando colunas 2 e 3) e armazenando os dados
                if x == 2:
                    codigo = info.text
                    dado["Numero"] = info.text
                elif x == 3:
                    codigo = f"{codigo}/{info.text}"
                    dado["Ano"] = info.text
                elif x <= 9:  # Limita o índice ao tamanho da lista 'colunas'
                    dado[colunas[x - 1]] = info.text

            if codigo:
                dicionario[codigo] = dado
        
        driver.back()
        time.sleep(1)
        driver.back()
        time.sleep(1)

    driver.quit()
    return dicionario

def process_all_urls(urls_file):
    urls = read_urls(urls_file)
    results = []
    for url in urls:
        try:
            result = get_LA(url)
            results.append(result)
        except Exception as e:
            print(f"Failed to process URL {url}: {e}")
    return results

# Chama a função para processar todas as URLs
dados_coletados = process_all_urls(urls_file)
print(dados_coletados)


