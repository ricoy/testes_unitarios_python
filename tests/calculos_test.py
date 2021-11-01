from unittest import TestCase
from application.calculos import Calculadora, ImpressaoCalculos

class TestCalculadora(TestCase):
    
    def test_constants_calculadora(self):
        self.assertEqual(Calculadora.OP_SOMA, 'soma')
        self.assertEqual(Calculadora.OP_SUBTRACAO, 'sub')
        self.assertEqual(Calculadora.OP_MULTIPLICACAO, 'multi')
        self.assertEqual(Calculadora.OP_DIVISAO, 'div')

    def test_calculos(self):
        calculadora = Calculadora()
        with self.assertRaises(ValueError):
            calculadora.calcular(1, 1, 'dafdadfa')
        self.assertEqual(2, calculadora.calcular(1, 1, Calculadora.OP_SOMA))
        self.assertEqual(0, calculadora.calcular(1, 1, Calculadora.OP_SUBTRACAO))
        self.assertEqual(15, calculadora.calcular(3, 5, Calculadora.OP_MULTIPLICACAO))
        self.assertEqual(5, calculadora.calcular(15, 3, Calculadora.OP_DIVISAO))

class TestImpressaoCalculos(TestCase):
    
    def test_impressao_calculos(self):
        imp = ImpressaoCalculos(Calculadora())
        calculos = imp.obter_calculos()
        self.assertIsInstance(calculos, list)

      
        

