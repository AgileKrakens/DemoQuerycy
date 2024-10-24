from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def web_driver(url2): 
    service = Service()
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    
    driver = webdriver.Firefox(service=service, options=options)
    driver.get(url2)
    time.sleep(2)
    return driver
    
def nome_social(url2):
    driver = web_driver(url2)
    data = driver.find_element(By.XPATH, '//*[@id="basicInformationSection"]/div[2]/dvg-candidato-dados/div/div[1]/label[2]').text
    return data, driver.quit()

def data_nasc(url2):
    driver = web_driver(url2)
    data = driver.find_element(By.XPATH, '//*[@id="basicInformationSection"]/div[2]/dvg-candidato-dados/div/div[2]/label[2]').text
    return data, driver.quit()
    
def ocupacao(url2):
    driver = web_driver(url2)
    data = driver.find_element(By.XPATH, '//*[@id="basicInformationSection"]/div[2]/dvg-candidato-dados/div/div[7]/label[2]').text
    return data, driver.quit()
    
def hist_mandatos(url2):
    driver = web_driver(url2)
    elemento = WebDriverWait(driver, 5).until( EC.element_to_be_clickable((By.XPATH, '//*[@id="mat-expansion-panel-header-2"]')) )
    elemento.click()
    time.sleep(3)
    
    data = driver.find_element(By.XPATH, '//*[@id="cdk-accordion-child-2"]/div/dvg-canditado-detalhe-eleicoes').text
    lines = data.strip().split('\n')
    result = []
    
    for line in lines:
        if 'Eleito' in line:
            index = line.index('Eleito')
            result.append(line[:index].strip())
        else:
            result.append(line.strip())
        
            
    return '\n'.join(result)
