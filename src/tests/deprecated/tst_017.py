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
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import TimeoutException

horaGlobal = time.strftime("%H%M%S")

class Test_017(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        # INGRESO A LA APP
        self.driver.get("https://www.spotify.com/ar/signup/?forward_url=https%3A%2F%2Fwww.spotify.com%2Far%2Fdownload%2F")


    def test_017(self):
        self.driver.find_element(By.ID,"register-email").send_keys("mervindiazlugo@gmail.com")

        self.driver.find_element(By.NAME, "signup_form[confirm_email]").send_keys("mervindiazlugo@gmail.com")

        self.driver.find_element(By.CSS_SELECTOR, "html.layout-signup body.page-signup.m-ar.l-es.is-loggedout.reboot div.wrap div.sign-up div.l-signup-body div.container div.l-box-content section.register div.content form#js-register-with-email fieldset ul li#li-thirdparty.thirdparty label.checkbox input#register-thirdparty.thirdparty").click()

        #self.driver.find_element(By.PARTIAL_LINK_TEXT, "y Condiciones de Uso").click()

        self.driver.find_element(By.XPATH, u"//*[contains(text(), 'Registr')]").click()

        #self.driver.get_screenshot_as_png()
        title = "Test_017"
        self.driver.get_screenshot_as_file(f"../data/capturas/{title}-{horaGlobal}.png")

        time.sleep(10)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()