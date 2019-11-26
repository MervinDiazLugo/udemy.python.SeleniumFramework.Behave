# -*- coding: utf-8 -*-
'''
Created on 11 oct. 2019

@author: Mervin
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_004(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        self.NOMBRE = "Mervin Alberto"
        self.APELLIDO = "Diaz Lugo"
        self.USERNAME = "MervinUdemytest2019"
        self.PASSWORD = "Udemytest2019-A"

    def test_004(self):
        
        #INGRESO A LA APP DE REGISTRO
        self.driver.get("https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp")
        
        #COLOCAR NOMBRE
        self.driver.find_element_by_id("firstName").clear()
        #self.driver.find_element_by_id("firstName").send_keys(self.NOMBRE)
        self.driver.find_element(By.ID, "firstName").send_keys(self.NOMBRE)
        
        #COLOCAR APELLIDO
        self.driver.find_element_by_xpath("//INPUT[@id='lastName']").clear()
        self.driver.find_element_by_xpath("//INPUT[@id='lastName']").send_keys(self.APELLIDO)

        #COLOCAR USERNAME
        self.driver.find_element_by_name("Username").clear()
        self.driver.find_element_by_name("Username").send_keys(self.USERNAME)

        #COLOCAR PASSWORD
        self.driver.find_element_by_xpath("(//*[@jsname='YPqjbf'])[5]").clear()
        self.driver.find_element_by_xpath("(//*[@jsname='YPqjbf'])[5]").send_keys(self.PASSWORD)

        #COLOCAR CONFIRMACION DE  PASSWORD
        self.driver.find_element_by_xpath("(//*[@jsname='YPqjbf'])[7]").clear()
        self.driver.find_element_by_xpath("(//*[@jsname='YPqjbf'])[7]").send_keys(self.PASSWORD)

        #BOTON NEXT
        self.driver.find_element_by_xpath("//*[@id='accountDetailsNext']").click()

        time.sleep(10)

        #MENSAJE DE VALIDACION
        MENSAJE_ERROR = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div[2]/form/div[1]/div/h1").text

        print(MENSAJE_ERROR)

        assert MENSAJE_ERROR == "Verificar tu número", "No coinciden"
        
    def tearDown(self):
        self.driver.quit()
        


if __name__ == "__main__":
    unittest.main()