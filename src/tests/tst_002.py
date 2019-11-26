from src.functions.Functions import Functions as Selenium
import unittest


class test_001(Selenium, unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self, "https://news.google.com/?hl=es-419&gl=AR&ceid=AR%3Aes-419", "IExplorer")

    def test_001(self):
        pass

    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main()
