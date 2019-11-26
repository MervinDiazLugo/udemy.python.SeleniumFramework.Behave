# -*- coding: utf-8 -*-
from src.functions.Functions import Functions as Selenium
from src.pages.Spotify_registro import Registro
import unittest
import time

class test_004(Selenium, unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self, URL= "https://chercher.tech/practice/frames-example-selenium-webdriver")

    def test_004(self):
        #cARGAR EL JSON CON LOS VALORES DE LOS ID DE  LA APP
        Selenium.get_json_file(self, "frames")
        Selenium.switch_to_iframe(self, "Frame2")
        Selenium.select_by_text(self, "Frame2 Select", "Avatar")
        Selenium.switch_to_parentFrame(self)

        Selenium.switch_to_iframe(self, "Frame1")
        Selenium.send_key_text(self, "Frame1 input", "Hola Chicos de Udemy")

        Selenium.switch_to_iframe(self, "Frame3")
        Selenium.get_elements(self, "Frame3 input").click()

        time.sleep(5)

    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main()
