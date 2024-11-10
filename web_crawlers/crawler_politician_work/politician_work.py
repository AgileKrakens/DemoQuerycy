import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


base_dir = os.path.dirname(__file__)  
urls_file = os.path.join(base_dir, "..", "crawler_personal_data", "camara_endpoints.txt")


def read_urls(urls_file):
    with open(urls_file, 'r') as f:
        urls = f.read().splitlines()
    return urls

def get_LA(url):
    service = Service()


    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")  
    options.add_argument("--no-sandbox")

    driver = webdriver.Firefox(service=service, options=options)
    driver.get(url)
    time.sleep(2)

    leis_de_autoria = driver.find_element(By.XPATH, '//*[@id="link_leis_autoria"]/a')
    leis_de_autoria.click()
    time.sleep(2)
    
    limite = 0
    for xpath in range(1, 6): 
        try:
            driver.find_element(By.XPATH, f'//*[@id="tab_leis_autoria"]/div/div[{xpath}]/div[1]/div/a')
            limite += 1
        except NoSuchElementException:
            continue

    dicionario = {} 
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
                    dado["Autor"] = info.text
                else:
                    info = driver.find_element(By.XPATH, f'//*[@id="relatorio"]/tr[{k}]/td[{x}]')

                
                if x == 2:
                    codigo = info.text
                    dado["Numero"] = info.text
                elif x == 3:
                    codigo = f"{codigo}/{info.text}"
                    dado["Ano"] = info.text
                elif x <= 9: 
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


dados_coletados = process_all_urls(urls_file)
print(dados_coletados)
