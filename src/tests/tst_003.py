# -*- coding: utf-8 -*-
from src.functions.Functions import Functions as Selenium
from src.pages.Spotify_registro import Registro
import unittest
import time


class test_003(Selenium, unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self)

    def test_003(self):

        assert Selenium.xpath_element(self, Registro.lbl_titulo_xpath).text == "Regístrate con tu dirección de email"
        print (Selenium.xpath_element(self, Registro.lbl_titulo_xpath).text)

        Selenium.xpath_element(self, Registro.txt_email_xpath).send_keys("mervindiazlugo@gmail.com")
        Selenium.xpath_element(self, Registro.txt_email_confirm_xpath).send_keys("mervindiazlugo@gmail.com")


        Selenium._id_element(self, Registro.txt_password_id).send_keys("Mmxxx20000")

        Selenium._id_element(self, Registro.txt_nombre_id).send_keys("Mervin Udemy")

        time.sleep(5)

    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main()
