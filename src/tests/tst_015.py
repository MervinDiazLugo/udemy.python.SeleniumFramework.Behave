# -*- coding: utf-8 -*-
from src.functions.Functions import Functions as Selenium
import unittest
import allure

@allure.feature(u'Test Udemy 1')
@allure.story(u'015: Visitamos google y colocamos una fecha')
@allure.testcase(u"Caso de Prueba 015", u'http://my.tms.org/browse/TESTCASE-39')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""Se requiere visitar el sitio googole:</br>
Deseamos ingresar texto en el recuadro de busqueda de google </br>
 </br></br>""")
class test_015(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1: Ingresar a Google'):
            self.CURSOR = Selenium.pyodbc_query(self, "SELECT * FROM my_api_subcategoria")
            Selenium.abrir_navegador(self, "https://www.google.com/")
            Selenium.get_json_file(self, "Google")

    def test_015(self):
        with allure.step(u'PASO 2: Ingresar termino de Busqueda'):
            date = Selenium.textDateEnvironmentReplace(self, "Last Month")

            Selenium.get_elements(self, "txt_busqueda").send_keys(date)

            Selenium.esperar(self, 10)


    def tearDown(self):
        with allure.step(u'PASO 3: Cerramos el navegador'):
            Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main()
