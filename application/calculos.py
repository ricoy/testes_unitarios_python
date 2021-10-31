class Calculadora:
    
    OP_SOMA = 'soma'
    OP_SUBTRACAO = 'sub'
    OP_DIVISAO = 'div'
    OP_MULTIPLICACAO = 'multi'

    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def calcular(self, operacao):
        if (operacao is self.OP_SOMA):
            return self.num_1 + self.num_2
        elif (operacao is self.OP_SUBTRACAO):
            return self.num_1 - self.num_2
        elif (operacao is self.OP_DIVISAO):
            return self.num_1/self.num_2
        elif (operacao is self.OP_MULTIPLICACAO):
            return self.num_1 * self.num_2
        
        raise ValueError('Operacao nao permitida')
