# -*- coding: utf-8 -*-
from src.functions.Functions import Functions as Selenium
import unittest
import time


class test_012(Selenium, unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self)
        Selenium.get_json_file(self, "Spotify_registro")

    def test_012(self):

        Selenium.save_variable_scenary(self, "Already", "Already")
        Selenium.save_variable_scenary(self, "Titulo", "Titulo")

        Selenium.new_window(self, "https://www.google.com/")
        Selenium.get_json_file(self, "Google")

        Selenium.switch_to_windows_name(self, "Google")

        texto = Selenium.get_variable_scenary(self, "Already")

        Selenium.get_elements(self, "txt_busqueda").send_keys(texto)

        Selenium.esperar(self, 10)


    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main()
