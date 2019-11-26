# -*- coding: utf-8 -*-
from src.functions.Functions import Functions as Selenium
import unittest
import time

class test_008(Selenium, unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self, URL= "https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert")
        Selenium.get_json_file(self, "frames")

    def test_008(self):
        Selenium.page_has_loaded(self)
        Selenium.switch_to_iframe(self, "Frame4 Alerta")
        Selenium.get_elements(self, "Alert").click()
        Selenium.esperar(self, 5)
        Selenium.alert_windows(self, "accept")
        Selenium.esperar(self, 5)


    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main()
