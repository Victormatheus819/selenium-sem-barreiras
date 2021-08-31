from os import times
from selenium.webdriver.common.keys import Keys
from  selenium  import webdriver
from  selenium.webdriver.support.ui import Select
import time



driver = webdriver.Chrome(executable_path=r"chromedriver.exe")
driver.get("https://sem-barreiras.herokuapp.com/")
but=driver.find_element_by_class_name("buttonFiltro")

but.click()


drpest = Select(driver.find_element_by_id("listEstado"))
time.sleep(1)
drpest.select_by_index(7)

driver.find_element_by_class_name("btn-confirm").click()