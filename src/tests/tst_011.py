# -*- coding: utf-8 -*-
from src.functions.Functions import Functions as Selenium
import unittest
import time


class test_011(Selenium, unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self)
        Selenium.get_json_file(self, "Spotify_registro")

    def test_011(self):

        Selenium.get_elements(self, "Email").send_keys("mervindiazlugo@gmail.com")
        Selenium.send_especific_keys(self, "Email", "Tab")

        verificar = Selenium.check_element(self, "Email Error")

        if verificar == True:
            #Selenium.send_key_text(self, "Email", "mervindiazlugo@gmail.com")
            unittest.TestCase.skipTest(self, "El email ya existe")

        time.sleep(5)

    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main()
