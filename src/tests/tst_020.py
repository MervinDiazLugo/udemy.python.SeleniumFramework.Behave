# -*- coding: utf-8 -*-
from src.functions.Functions import Functions as Selenium
import unittest
import pytest


class test_020(unittest.TestCase, Selenium):

    def setUp(self):
        Selenium.abrir_navegador(self)
        Selenium.get_json_file(self, "Spotify_registro")

    def test_020(self):
        Selenium.get_elements(self, "Email").send_keys("mervindiazlugo@gmail.com")
        Selenium.get_elements(self, "Email Confirmacion").click()

        #Mensaje_Email = Selenium.validar_elemento(self, "Mensaje Email")
        Captcha = Selenium.validar_elemento(self, "Contenedor Captcha")

        #print(Mensaje_Email)

        if Captcha:
            pytest.skip("No se ejecuto la prueba, captcha esta visible")
            #unittest.TestCase.skipTest(self, "No se ejecuto la prueba captcha esta visible")


    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main()
