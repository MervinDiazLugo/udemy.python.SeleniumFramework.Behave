# -*- coding: utf-8 -*-
from src.functions.Functions import Functions as Selenium
from src.pages.Spotify_registro import Registro
import unittest
import time

class test_004(Selenium, unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self, URL= "https://www.mercadolibre.com.ar/")

    def test_004(self):

        Selenium.new_window(self, "https://www.mercadolibre.com.ar/ofertas#nav-header")

        Selenium.switch_to_windows_name(self, "Ofertas")

        time.sleep(5)

        Selenium.switch_to_windows_name(self, "Principal")

        time.sleep(5)

        Selenium.switch_to_windows_name(self, "Ofertas")

    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main()
