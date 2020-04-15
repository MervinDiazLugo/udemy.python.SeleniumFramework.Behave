import unittest
import pytest

class test_002(unittest.TestCase):

    def setUp(self):
        pass


    def test_comparacion(self):
        self.Variable_A = 51
        self.Variable_B = 50

        assert self.Variable_A != self.Variable_B, "Los valores son distintos"

    def test_004(self):
        self.Variable_A = 2

        if self.Variable_A < 3:
            pytest.skip("El valor es muy inferior para ejecutar la prueba")

        if self.Variable_A >= 10:
            self.Resultado = True

        else:
            self.Resultado = False

        assert self.Resultado, f"El valor no es mayor es: {self.Variable_A}"

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
