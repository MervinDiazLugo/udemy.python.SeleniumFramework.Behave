# -*- coding: utf-8 -*-
'''
Created on 11 oct. 2019

@author: Mervin
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By



class Test_007(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        self.NOMBRE = "Mervin Alberto"
        self.APELLIDO = "Diaz Lugo"
        self.USERNAME = "MervinUdemytest2019"
        self.PASSWORD = "Udemytest2019-A"

    def test_007(self):
        
        #INGRESO A LA APP DE REGISTRO
        self.driver.get("https://autos.mercadolibre.com.ar/sedan/_DisplayType_LF")
        
        time.sleep(5)
        
        #self.LISTADO = self.driver.find_elements_by_xpath("//*[contains(@class, 'main-title')]")
        self.LISTADO = self.driver.find_elements(By.XPATH, "//*[contains(@class, 'main-title')]")
        self.LISTADO2 = self.driver.find_elements(By.XPATH, "//*[contains(@class, 'product-attributes')]")
        
        print ("listado de elementos encontrados" + str(self.LISTADO))
        
        self.count = 0
        
        for self.lista in self.LISTADO:
            
            print(self.lista.text)
            
        for self.lista2 in self.LISTADO2:
            print(self.lista2.text)
            
            
            
            
        

        
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()