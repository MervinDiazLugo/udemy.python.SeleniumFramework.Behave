# -*- coding: utf-8 -*-
'''
Created on 11 oct. 2019

@author: Mervin
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import TimeoutException



class Test_012(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        # INGRESO A LA APP DE REGISTRO
        self.driver.get("http://www.echoecho.com/htmllinks10.htm")

    def test_012(self):
        #MAIN
        self.main_Enlace = self.driver.find_element_by_xpath("//span[contains(text(),'Go to Yahoo')]")
        self.main_Enlace.click()

        print("Ventanas" + str(self.driver.window_handles))

        time.sleep(10)

        self.driver.switch_to.window(self.driver.window_handles[0])

        self.main_Enlace.click()
        time.sleep(10)

        print("Ventanas" + str(self.driver.window_handles))



        time.sleep(10)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()