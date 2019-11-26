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



class Test_013(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        # INGRESO A LA APP
        self.driver.get("https://www.mercadolibre.com.ar/")

    def test_013(self):

        localizador = self.driver.find_element(By.XPATH,
                                               "/html[1]/body[1]/header[1]/div[1]/div[2]/ul[1]/li[2]/a[1]")

        action = ActionChains(self.driver)

        action.move_to_element(localizador)
        action.perform()

        localizador2 = self.driver.find_element(By.XPATH,
                                                "/html[1]/body[1]/header[1]/div[1]/div[2]/ul[1]/li[2]/nav[1]/section[1]/ul[2]/li[1]/a[1]")
        action.move_to_element(localizador2)
        action.perform()

        time.sleep(5)

        localizador3 = self.driver.find_element(By.XPATH,
                                                "/html[1]/body[1]/header[1]/div[1]/div[2]/ul[1]/li[2]/nav[1]/section[2]/div[1]/div[1]/article[1]/h2[1]/a[1]")
        localizador3.click()

        time.sleep(10)


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()