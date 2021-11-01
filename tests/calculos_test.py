from unittest import TestCase
from unittest.mock import patch, Mock

from application.calculos import Calculadora, ImpressaoCalculos

class TestCalculadora(TestCase):
    
    def test_verifica_valores_constantes_calculadora(self):
        self.assertEqual(Calculadora.OP_SOMA, 'soma')
        self.assertEqual(Calculadora.OP_SUBTRACAO, 'sub')
        self.assertEqual(Calculadora.OP_MULTIPLICACAO, 'multi')
        self.assertEqual(Calculadora.OP_DIVISAO, 'div')

    def test_verifica_retorno_calculos(self):
        calculadora = Calculadora()
        with self.assertRaises(ValueError):
            calculadora.calcular(1, 1, 'dafdadfa')
        self.assertEqual(2, calculadora.calcular(1, 1, Calculadora.OP_SOMA))
        self.assertEqual(0, calculadora.calcular(1, 1, Calculadora.OP_SUBTRACAO))
        self.assertEqual(15, calculadora.calcular(3, 5, Calculadora.OP_MULTIPLICACAO))
        self.assertEqual(5, calculadora.calcular(15, 3, Calculadora.OP_DIVISAO))

class TestImpressaoCalculos(TestCase):
    
    def test_verifica_formato_obtencao_calculos(self):
        imp = ImpressaoCalculos(Calculadora())
        calculos = imp.obter_calculos()
        self.assertIsInstance(calculos, list)
        self.assertIsInstance(calculos[0], tuple)

    @patch('application.calculos.Calculadora')
    def test_verifica_metodo_chamado_impressao_calculos(self, MockCalculadora):
        MockCalculadora.calcular = Mock(spec=[], name="calcular", return_value = 1)
        imp = ImpressaoCalculos(MockCalculadora)
        imp.imprimir()
        MockCalculadora.calcular.assert_called_with(10, 2, MockCalculadora.OP_DIVISAO)

      
        

