# -*- coding: utf-8 -*-
from src.functions.Functions import Functions as Selenium
import unittest

class test_009(Selenium, unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self, URL= "https://www.google.com/")
        Selenium.get_json_file(self, "Google")

    def test_009(self):
        Selenium.page_has_loaded(self)
        Selenium.get_elements(self, "txt_busqueda").click()

        Selenium.get_elements(self, "txt_busqueda").send_keys("Selenium Udemy")
        #Selenium.send_key_text(self, "txt_busqueda", "Selenium Udemy")

        Selenium.esperar(self, 5)

        Selenium.send_especific_keys(self, "txt_busqueda", "Enter")
        Selenium.esperar(self, 5)


    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main()
