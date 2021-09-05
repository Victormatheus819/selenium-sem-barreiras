
from os import times
from selenium.webdriver.common.keys import Keys
from  selenium  import webdriver
from  selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome(executable_path=r"chromedriver.exe")
driver.get("http://localhost:8080/")
but=driver.find_element_by_class_name("buttonFiltro")

but.click()


drpemp = Select(driver.find_element_by_id("listEmpresa"))
time.sleep(5)
drpemp.select_by_index(1)
drpest = Select(driver.find_element_by_id("listEstado"))
time.sleep(1)
drpest.select_by_index(1)
drpesc = Select(driver.find_element_by_id("listEscolaridade"))
time.sleep(1)
drpesc.select_by_index(9)
drparea = Select(driver.find_element_by_id("listArea"))
time.sleep(1)
drparea.select_by_index(18)
drpdef = Select(driver.find_element_by_id("listDeficiencia"))
time.sleep(1)
drpdef.select_by_index(1)
remu=driver.find_element_by_id("remuneracao")

remu.send_keys("1000")

driver.find_element_by_class_name("btn-confirm").click()

textResult = driver.find_element_by_id("textoResultado")


if(textResult.text == "1 resultados"):
    print ("Teste de combinação de todos os filtros com sucesso !!!\n")
