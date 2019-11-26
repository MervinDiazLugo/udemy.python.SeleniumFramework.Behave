# -*- coding: utf-8 -*-
from src.functions.Functions import Functions as Selenium
import unittest
import time


class test_010(Selenium, unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self)
        Selenium.get_json_file(self, "Spotify_registro")

    def test_010(self):

        Selenium.get_elements(self, "Email").send_keys("mervlugo@gmailcom")
        Selenium.send_especific_keys(self, "Email", "Tab")

        Selenium.assert_text(self, "Email Error", "La dirección de email que proporcionaste no es válida.")

        time.sleep(5)

    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main()
