from os import times
from selenium.webdriver.common.keys import Keys
from  selenium  import webdriver
from  selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome(executable_path=r"chromedriver.exe")
driver.get("http://localhost:8080/")

cursos=driver.find_element_by_id("curso")
time.sleep(2)
cursos.click()

but=driver.find_element_by_class_name("buttonFiltro")
time.sleep(2)
but.click()
time.sleep(2)
prec= driver.find_element_by_id("precoMinimo")
time.sleep(2)
prec.send_keys("39.4")

driver.find_element_by_class_name("btn-confirm").click()


cursodesc=driver.find_element_by_id("1")
time.sleep(2)
cursodesc.click()



if( driver.current_url == "https://www.udemy.com/course/curso-de-programacao-em-python-do-basico-ao-avancado/"):
    print ("\nTeste de filtro de curso feito com sucesso  !!!\n")
