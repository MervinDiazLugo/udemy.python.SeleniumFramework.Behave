# -*- coding: utf-8 -*-
from src.functions.Functions import Functions as Selenium
from src.pages.Spotify_registro import Registro
import unittest
import time

class test_007(Selenium, unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self, URL= "https://www.amazon.es/")

    def test_007(self):
        Selenium.get_json_file(self, "Amazon")
        Selenium.scroll_to(self, "Sobre Amazon")
        Selenium.esperar(5)
        Selenium.js_clic(self, "Sobre Amazon")
        Selenium.page_has_loaded(self)


    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main()
