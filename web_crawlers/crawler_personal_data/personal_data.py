from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service()

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(service=service, options=options)

url = 'https://divulgacandcontas.tse.jus.br/divulga/#/candidato/SUDESTE/SP/2030402020/250000753710/2020/70998'

driver.get(url)
time.sleep(5)

nome_vereador = driver.find_element(By.XPATH, '//*[@id="basicInformationSection"]/div[2]/dvg-candidato-dados/div/div[1]/label[2]')
data_nascimento_vereador = driver.find_element(By.XPATH, '//*[@id="basicInformationSection"]/div[2]/dvg-candidato-dados/div/div[2]/label[2]')
genero_vareador = driver.find_element(By.XPATH, '//*[@id="basicInformationSection"]/div[2]/dvg-candidato-dados/div/div[3]/label[2]')
cor_vereador = driver.find_element(By.XPATH, '//*[@id="basicInformationSection"]/div[2]/dvg-candidato-dados/div/div[4]/label[2]')
grau_intituição = driver.find_element(By.XPATH, '//*[@id="basicInformationSection"]/div[2]/dvg-candidato-dados/div/div[6]/label[2]')
nacionalidade = driver.find_element(By.XPATH, '//*[@id="basicInformationSection"]/div[2]/dvg-candidato-dados/div/div[8]/label[2]')
ocupacao = driver.find_element(By.XPATH, '//*[@id="basicInformationSection"]/div[2]/dvg-candidato-dados/div/div[7]/label[2]')

elemento = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="mat-expansion-panel-header-2"]'))
)

elemento.click()
time.sleep(3)
partido = driver.find_element(By.XPATH, '//*[@id="cdk-accordion-child-2"]/div/dvg-canditado-detalhe-eleicoes')

print(nome_vereador.text, data_nascimento_vereador.text, genero_vareador.text, cor_vereador.text, grau_intituição.text, nacionalidade.text, ocupacao.text)

texto = partido.text
linhas = texto.strip().split('\n')

resultado = []
for linha in linhas:
    if 'Eleito' in linha:

        indice_eleito = linha.index('Eleito')

        resultado.append(linha[:indice_eleito].strip())  
    else:
        resultado.append(linha.strip()) 

print('\n'.join(resultado))


driver.quit()
