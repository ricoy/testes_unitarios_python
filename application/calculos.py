class Calculadora:
    
    OP_SOMA = 'soma'
    OP_SUBTRACAO = 'sub'
    OP_DIVISAO = 'div'
    OP_MULTIPLICACAO = 'multi'

    def calcular(self, num_1, num_2, operacao):
        if (operacao is self.OP_SOMA):
            return num_1 + num_2
        elif (operacao is self.OP_SUBTRACAO):
            return num_1 - num_2
        elif (operacao is self.OP_DIVISAO):
            return num_1/num_2
        elif (operacao is self.OP_MULTIPLICACAO):
            return num_1 * num_2
        
        raise ValueError('Operacao nao permitida')

class ImpressaoCalculos:
    def __init__(self, calculadora):
        self.calculadora = calculadora
    
    def obter_calculos(self):
        return [
            (1, 1, Calculadora.OP_SOMA),
            (5, 2, Calculadora.OP_MULTIPLICACAO),
            (10, 2, Calculadora.OP_DIVISAO)
        ]

    def imprimir(self):
        for calculo in self.obter_calculos():
            print(self.calculadora.calcular(*calculo))

if __name__ == '__main__':
    calculadora = Calculadora()
    print(calculadora.calcular(5, 3, Calculadora.OP_MULTIPLICACAO))
    # imp = ImpressaoCalculos(calculadora)
    # imp.imprimir()