import abc
from unittest import TesteCase, main

class Calculadora(object):
    def calcular(self, valor1, valor2, operador):
        operacaoEscolhida = escolhaOperacao()
        operacao = operacaoEscolhida.criar(operador)
        if (operador == None):
            return 0
        else:
            resultado = operacao.executar(valor1, valor2)
            return resultado

class escolhaOperacao(object):
    def criar(self, operador):
        if(operador == 'soma'):
            return Soma()
        elif(operador == 'subtracao'):
            return Subtracao()
        elif(operador == 'divisao'):
            return Divisao()
        elif(operador == 'multiplicacao'):
            return Multiplicacao()

class Operacao(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def executar(self, valor1, valor2):
        pass

class Soma(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 + valor2
        return resultado

class Subtracao(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 - valor2
        return resultado

class Divisao(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 / valor2
        return resultado

class Multiplicacao(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 * valor2
        return resultado


class testesUnitarios(TestCase):

    def test_soma(self):
        calculadora = Calculadora()
        result = calculadorSoma.calcular(5,5,'soma')
        self.assertEqual(result, 10)

    def test_subtracao(self):
        calculadora = Calculadora()
        result = calculadorSubtracao.calcular(10,5,'subtracao')
        self.assertEqual(result, 10)

    def test_multiplicacao(self):
        calculadora = Calculadora()
        result = calculadorSoma.calcular(5,5,'multiplicacao')
        self.assertEqual(result, 25)

    def test_divisao(self):
        calculadora = Calculadora()
        result = calculadorSoma.calcular(10,2,'divisao')
        self.assertEqual(result, 5)







