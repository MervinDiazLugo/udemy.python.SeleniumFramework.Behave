# -*- coding: utf-8 -*-
'''
Created on 11 oct. 2019

@author: Mervin
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import TimeoutException



class Test_010(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()


    def test_010(self):
        
        #INGRESO A LA APP DE REGISTRO
        self.driver.get("https://www.mercadolibre.com.ar")
        
        self.element = "/html[1]/body[1]/main[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]"
        
        self.element1 = "//*[@class='af']"
        
        try:
            wait = WebDriverWait(self.driver, 15)
            wait.until(EC.visibility_of_element_located((By.XPATH, self.element1)))
            
        except TimeoutException: 
            self.skipTest("No se encontro el elemento")

        
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()