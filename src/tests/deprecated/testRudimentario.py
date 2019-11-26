'''
Created on 10 oct. 2019

@author: Mervin
'''
###### IMPORTANDO LIBRERIAS DE SELENIUM
from selenium import webdriver
import time


###### INICIALIZO EL DRIVER
driver = webdriver.Chrome()

### VOY HOST DE LA APLICACION
driver.get("http://www.python.org")

#SE VERIFICA QUE EL TITULO DE LA APLICACION
assert "Python" in driver.title

time.sleep(10)

###### ALMACENO EN UNA VARIABLE EL OBJETO CON QUE VOY A INTERACTUAR
elem = driver.find_element_by_id("id-search-field")

###lIMPIO LA TXT
elem.clear()

###ESCRRIBO PYCON
elem.send_keys("pycon")

time.sleep(10)

#CIEROO EL DRIVER
driver.close()