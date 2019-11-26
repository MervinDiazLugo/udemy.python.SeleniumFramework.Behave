# -*- coding: utf-8 -*-
'''
Created on 11 oct. 2019

@author: Mervin
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import TimeoutException



class Test_014(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        # INGRESO A LA APP
        self.driver.get("https://www.amazon.es/")

        time.sleep(5)

    def test_014(self):
        localizador = self.driver.find_element(By.XPATH,
                                               "/html[1]/body[1]/div[1]/div[4]/div[1]/div[1]/div[1]/ul[1]/li[2]/a[1]")
        self.driver.execute_script("arguments[0].scrollIntoView();", localizador)

        localizador = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[4]/div[1]/div[1]/div[1]/ul[1]/li[2]/a[1]")
        self.driver.execute_script("arguments[0].click();", localizador)

        time.sleep(5)
        assert "Sobre Amazon" ==  self.driver.title,  "No son iguales"


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()