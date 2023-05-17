import time
import datetime
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


hora_desejada = datetime.time(13,0,0)


def ponto():
    url = "https://app.tangerino.com.br/Tangerino/pages/LoginPage"
    options = webdriver.ChromeOptions()
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-session-crashed-bubble")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--incognito")    
    driver = webdriver.Chrome(executable_path=r'.\bin\chromedriver.exe', chrome_options=options)
    driver.maximize_window()
    driver.get(url)
    driver.find_element(By.XPATH,'//*[@id="id7"]/fieldset/ul/li[3]/a').click()
    driver.find_element(By.XPATH,'//*[@id="codigoEmpregador"]').send_keys("YPS86")
    driver.find_element(By.XPATH,'//*[@id="codigoPin"]').send_keys("9794")
    driver.find_element(By.XPATH,'//*[@id="registraPonto"]/span[1]').click()
    return driver



while True: 
    hora_atual = datetime.datetime.now().time()
    if hora_atual.hour == hora_desejada.hour and hora_atual.minute == hora_desejada.minute:
        ponto()
        time.sleep(4068)
        driver = ponto()
        break

driver.quit()
    




