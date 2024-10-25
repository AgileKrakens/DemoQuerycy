from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

tipos_de_proposta = ['//*[@id="tab_leis_autoria"]/div/div[1]/div[1]/div/a', '//*[@id="tab_leis_autoria"]/div/div[2]/div[1]/div/a', '//*[@id="tab_leis_autoria"]/div/div[3]/div[1]/div/a',
                    '//*[@id="tab_leis_autoria"]/div/div[4]/div[1]/div/a', '//*[@id="tab_leis_autoria"]/div/div[5]/div[1]/div/a']

def get_LA(url2):
    url = url2
    service = Service()

    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(service=service, options=options)

    driver.get(url)
    time.sleep(2)

    leis_de_autoria = driver.find_element(By.XPATH, '//*[@id="link_leis_autoria"]/a')

    leis_de_autoria.click()
    time.sleep(2)

    la = driver.find_element(By.XPATH, f'{tipos_de_proposta[3]}')
    la.click()
    time.sleep(2)

    press = driver.find_element(By.XPATH, '//*[@id="btn_impressao"]')
    press.click()

    qtd = driver.find_element(By.XPATH, '//*[@id="total"]/h1[1]/strong').text
    qtd = int(qtd)
    dicionario = {}

    for k in range (1,qtd+1):
        dado = []
        codigo = None
        for x in range (1,10):
            if x == 6:
                continue
            info = driver.find_element(By.XPATH, f'//*[@id="relatorio"]/tr[{k}]/td[{x}]')
            
            if x == 5:
                continue

            if x == 2:
                codigo = info.text
                dado.append(info.text)
            else:
                dado.append(info.text)

        if codigo:
            dicionario[codigo] = dado

    return dicionario

preposicoes = ['//*[@id="tab_proposicoes_apresentadas"]/div/div[2]/div[1]/div/a/span', '//*[@id="tab_proposicoes_apresentadas"]/div/div[2]/div[1]/div/a', '//*[@id="tab_proposicoes_apresentadas"]/div/div[3]/div[1]/div/a', '//*[@id="tab_proposicoes_apresentadas"]/div/div[4]/div[1]/div/a',
               '//*[@id="tab_proposicoes_apresentadas"]/div/div[5]/div[1]/div/a', '//*[@id="tab_proposicoes_apresentadas"]/div/div[6]/div[1]/div/a', '//*[@id="tab_proposicoes_apresentadas"]/div/div[7]/div[1]/div/a',
               '//*[@id="tab_proposicoes_apresentadas"]/div/div[8]/div[1]/div/a', '//*[@id="tab_proposicoes_apresentadas"]/div/div[9]/div[1]/div/a', '//*[@id="tab_proposicoes_apresentadas"]/div/div[10]/div[1]/div/a']

def get_Prepositions(url2):
    url = url2
    service = Service()

    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(service=service, options=options)

    driver.get(url)
    time.sleep(2)

    leis_de_autoria = driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_acessibilidade_padrao"]/div/div/div[2]/div/div[1]/div[2]/ul/li[2]/a')

    leis_de_autoria.click()
    time.sleep(2)

    prep = driver.find_element(By.XPATH, f'{preposicoes[2]}')
    prep.click()
    time.sleep(2)

    count = int(driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_contagem"]/strong').text)
    if count >= 1000:
        return 'Busca possui mais de 1000 resultados.'
    


    press = driver.find_element(By.XPATH, '//*[@id="btn_impressao"]')
    press.click()

    qtd = driver.find_element(By.XPATH, '//*[@id="total"]/h1[1]/strong').text
    qtd = int(qtd)
    dicionario = {}


    for k in range (1,qtd+1):
        dado = []
        codigo = None
        for x in range (1,10):
            if x == 6:
                continue
            info = driver.find_element(By.XPATH, f'//*[@id="relatorio"]/tr[{k}]/td[{x}]')

            if info.text == '':
                continue

            if x == 6:
                continue

            if x == 1:
                codigo = info.text
                dado.append(info.text)
            else:
                dado.append(info.text)
            

        if codigo:
            dicionario[codigo] = dado

    return dicionario

print(get_Prepositions('https://camarasempapel.camarasjc.sp.gov.br/spl/parlamentar.aspx?id=245'))

# //*[@id="relatorio"]/tr[1]/td[1]