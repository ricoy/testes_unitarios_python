from unittest import TestCase
from application.calculos import Calculadora

class TestCalculadora(TestCase):
    def test_calculos(self):
        calculadora = Calculadora(1, 1)
        with self.assertRaises(ValueError):
            calculadora.calcular(1)

        with not self.assertRaises(ValueError):
            self.assertEqual(2, calculadora.calcular(Calculadora.OP_SOMA))
            
        self.assertEqual(2, calculadora.calcular(Calculadora.OP_SOMA))
        self.assertEqual(0, calculadora.calcular(Calculadora.OP_SUBTRACAO))
        self.assertEqual(1, calculadora.calcular(Calculadora.OP_MULTIPLICACAO))
        self.assertEqual(1, calculadora.calcular(Calculadora.OP_DIVISAO))
        

