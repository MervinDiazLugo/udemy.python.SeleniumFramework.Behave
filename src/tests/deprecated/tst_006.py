# -*- coding: utf-8 -*-
'''
Created on 11 oct. 2019

@author: Mervin
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Test_006(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        self.NOMBRE = "Mervin Alberto"
        self.APELLIDO = "Diaz Lugo"
        self.USERNAME = "MervinUdemytest2019"
        self.PASSWORD = "Udemytest2019-A"

    def test_006(self):
        
        #INGRESO A LA APP DE REGISTRO
        self.driver.get("https://www.correoargentino.com.ar/servicios/paqueteria")
        
        #COLOCAR BUSQUEDA
        self.driver.find_element_by_id("edit-custom-search-blocks-form-1--2").send_keys("DNI")
        
        
        #MANEJANDO SELECTS | DROPDOWNS
        select = Select(self.driver.find_element(By.ID, "edit-custom-search-vocabulary-8"))
        select.select_by_visible_text("Nacional")
        

        time.sleep(10)
        
        
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()