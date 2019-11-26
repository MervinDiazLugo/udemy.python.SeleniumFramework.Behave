# -*- coding: utf-8 -*-
from src.functions.Functions import Functions as Selenium
import unittest


class test_013(Selenium, unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self)
        Selenium.get_json_file(self, "Spotify_registro")

    def test_013(self):

        Selenium.save_variable_scenary(self, "Already", "Ya Tengo")

        Selenium.new_window(self, "https://www.spotify.com/py/signup/")

        Selenium.switch_to_windows_name(self, "Spoty Signup")

        Selenium.esperar_elemento(self, "Already")

        Selenium.compare_with_variable_scenary(self, "Already", "Ya Tengo")

        Selenium.esperar(self, 10)

        #RECUPERAR DESDE EXCEL
        NOMBRE = Selenium.leer_celda(self, "A1")
        APELLIDO = Selenium.leer_celda(self, "B1")
        DNI = Selenium.leer_celda(self, "C1")

        Selenium.create_variable_scenary(self, "NOMBRE", NOMBRE)
        Selenium.create_variable_scenary(self, "APELLIDO", Selenium.leer_celda(self, "B1"))


    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main()
