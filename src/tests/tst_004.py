# -*- coding: utf-8 -*-
from src.functions.Functions import Functions as Selenium
from src.pages.Spotify_registro import Registro
import unittest
import time

class test_004(Selenium, unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self)

    def test_004(self):
        #cARGAR EL JSON CON LOS VALORES DE LOS ID DE  LA APP
        Selenium.get_json_file(self, "Spotify_registro")

        #ACCEDER A LAS KEYS (ENTIDADES) DEL JSON
        Selenium.get_entity(self, "Logo")

        assert Selenium.get_text(self, "Titulo") == "Regístrate con tu dirección de email"

        Selenium.esperar_elemento(self, "Email")

        Selenium.get_elements(self, "Email").send_keys("merin@gmail.com")

        Selenium.esperar_elemento(self, "Email Confirmacion")

        Selenium.get_elements(self, "Email Confirmacion").send_keys("merin@gmail.com")

        Selenium.get_elements(self, "Pass").send_keys("skajdfhlksdjfhdsjfajskd")

        Selenium.get_elements(self, "Nombre").send_keys("Mervin Díaz")

        Selenium.get_select_elements(self, "Mes de Nacimiento").select_by_visible_text("enero")

        time.sleep(5)

    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main()
