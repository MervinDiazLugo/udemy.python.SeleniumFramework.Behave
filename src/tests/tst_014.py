# -*- coding: utf-8 -*-
from src.functions.Functions import Functions as Selenium
import unittest
import allure

@allure.feature(u'Test Udemy 1')
@allure.story(u'016: Capturas de pantalla')
@allure.testcase(u"Caso de Prueba 014", u'http://my.tms.org/browse/TESTCASE-39')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""Se requiere visitar el sitio googole:</br>
Deseamos ingresar texto en el recuadro de busqueda de google </br>
 </br></br>""")
class test_014(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1: Ingresar a Google'):
            Selenium.abrir_navegador(self, "https://www.google.com/")
            Selenium.get_json_file(self, "Google")

    def test_012(self):
        with allure.step(u'PASO 2: -----'):
            date = Selenium.textDateEnvironmentReplace(self, "Last Month")

            Selenium.get_elements(self, "txt_busqueda").send_keys(date)

            Selenium.esperar(self, 10)


    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main()
