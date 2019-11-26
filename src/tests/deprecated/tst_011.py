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



class Test_011(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        # INGRESO A LA APP DE REGISTRO
        self.driver.get("https://chercher.tech/practice/frames-example-selenium-webdriver")

    def test_010(self):
        #MAIN
        self.main_Titulo = self.driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]")
        print (self.main_Titulo.text)

        time.sleep(5)

        #FRAME2
        self.frame2 = self.driver.find_element_by_xpath("//iframe[@id='frame2']")
        self.driver.switch_to.frame(self.frame2)

        self.frame2_Select = Select(self.driver.find_element_by_xpath("//select[@id='animals']"))
        self.frame2_Select.select_by_visible_text('Baby Cat')
        time.sleep(5)

        #VOLVER AL MAIN
        self.driver.switch_to.parent_frame()

        # FRAME1
        self.frame1 = self.driver.find_element_by_xpath("//iframe[@id='frame1']")
        self.driver.switch_to.frame(self.frame1)
        self.frame1_text = self.driver.find_element_by_xpath("/html[1]/body[1]/input[1]")
        self.frame1_text.send_keys("Hola Chicos UDEMY")
        time.sleep(5)

        # FRAME3
        self.frame3 = self.driver.find_element_by_xpath("//iframe[@id='frame3']")
        self.driver.switch_to.frame(self.frame3)
        self.frame3_CheckBok = self.driver.find_element_by_xpath("//input[@id='a']")
        self.frame3_CheckBok.click()

        time.sleep(10)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()