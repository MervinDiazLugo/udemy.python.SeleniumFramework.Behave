import unittest

class test_002(unittest.TestCase):

    def setUp(self):
        pass


    def test_002(self):
        self.Variable_A = 50
        self.Variable_B = 50

        self.assertEqual(self.Variable_A, self.Variable_B, "Los valores son distintos")

    def test_003(self):
        self.Variable_A = 40
        self.Variable_B = 50

        self.assertNotEqual(self.Variable_A, self.Variable_B, "Los valores no son distintos")


    def test_004(self):
        self.Variable_A = 2

        if self.Variable_A < 3:
            unittest.TestCase.skipTest(self, "El valor es muy inferior para ejecutar la prueba")

        if self.Variable_A >= 10:
            self.Resultado = True

        else:
            self.Resultado = False

        self.assertTrue(self.Resultado, f"El valor no es mayor es: {self.Variable_A}")


    def test_005(self):
        self.Variable_A = "Bienvenido a la clase de unittest"
        self.Variable_B = "XXXX"

        self.assertIn(self.Variable_B, self.Variable_A, f"No coinciden")

    def test_006(self):
        self.Variable_A = "Bienvenido a la clase de unittest"
        self.Variable_B = "Bienvenido a la clase de unittest"

        self.assertIsNot(self.Variable_B, self.Variable_A, f"No coinciden")

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
