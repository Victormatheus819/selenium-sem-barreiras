from os import times
from selenium.webdriver.common.keys import Keys
from  selenium  import webdriver
from  selenium.webdriver.support.ui import Select
import time



driver = webdriver.Chrome(executable_path=r"chromedriver.exe")
driver.get("http://localhost:8080/")
but=driver.find_element_by_class_name("buttonFiltro")
but.click()
drpest = Select(driver.find_element_by_id("listEscolaridade"))
time.sleep(1)
drpest.select_by_index(8)

driver.find_element_by_class_name("btn-confirm").click()

textResult = driver.find_element_by_id("textoResultado")


if(textResult.text == "2 resultados"):
    print ("\nTeste  filtro de escolaridade com sucesso !!!\n")