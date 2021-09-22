from abc import abstractmethod, ABC as Abstract
from unittest import TestCase, main

''' Implementação '''

class Calculadora(object):
    def calcular(valor1, valor2, operador):

        operacao = OperacaoFabrica.criar(operador)
        if operacao == None:
            return 'Erro: Operação inválida'
        resultado = operacao.executar(valor1, valor2)
        return resultado


class OperacaoFabrica(object):
    def criar(operador):
        if operador == '+':
            return Soma()
        if operador == '-':
            return Subtracao()
        if operador == '*':
            return Multiplicacao()
        if operador == '/':
            return Divisao()
            

class Operacao(Abstract):
    @abstractmethod
    def executar(valor1, valor2):
        pass


class Soma(Operacao):
    def executar(self, valor1, valor2):
        return valor1 + valor2


class Subtracao(Operacao):
    def executar(self, valor1, valor2):
        return valor1 - valor2


class Multiplicacao(Operacao):
    def executar(self, valor1, valor2):
        return valor1 * valor2


class Divisao(Operacao):
    def executar(self, valor1, valor2):
        if valor2 == 0:
            return 'Erro: Impossível dividir por 0'
        return valor1 / valor2


''' Testes '''


class TestCalculadora(TestCase):
    def test_operacoes_calculadora(self):
        operadores_validos = {'+': Soma, '-': Subtracao, '*' : Multiplicacao, '/': Divisao}
        for operador in operadores_validos:
            resultado = Calculadora.calcular(3, 2, operador)
        self.assertTrue(isinstance(resultado, int) or isinstance(resultado, float))


class TestOperacaoFabrica(TestCase):
    def test_operacao_correta_instanciada(self):
        operadores_validos = {'+': Soma, '-': Subtracao, '*' : Multiplicacao, '/': Divisao}
        for operador,operacao in operadores_validos.items():
            operacao_fabricada = OperacaoFabrica.criar(operador)
            self.assertIsInstance(operacao_fabricada, operacao)
    
    def test_operacao_invalida_instanciada(self):
        operadores_invalidos = ['a', '++', '3']
        for operador in operadores_invalidos:
            resultado = OperacaoFabrica.criar(operador)
            self.assertEqual(resultado, None)


class TestSoma(TestCase):
    def test_soma_comum(self):
        resultado = Calculadora.calcular(1,1,'+')
        self.assertEqual(resultado, 2)

    def test_soma_negativos(self):
        resultado = Calculadora.calcular(-2,-3,'+')
        self.assertEqual(resultado, -5)


class TestSubtracao(TestCase):
    def test_subtracao_comum(self):
        resultado = Calculadora.calcular(4,2,'-')
        self.assertEqual(resultado, 2)

    def test_subtracao_negativos(self):
        resultado = Calculadora.calcular(-2,-3,'-')
        self.assertEqual(resultado, 1)


class TestMultiplicacao(TestCase):
    def test_multiplicacao_comum(self):
        resultado = Calculadora.calcular(4,2,'*')
        self.assertEqual(resultado, 8)

    def test_multiplicacao_negativos(self):
        resultado = Calculadora.calcular(-2,-3,'*')
        self.assertEqual(resultado, 6)


class TestMultiplicacao(TestCase):
    def test_multiplicacao_comum(self):
        resultado = Calculadora.calcular(4,2,'*')
        self.assertEqual(resultado, 8)

    def test_multiplicacao_negativos(self):
        resultado = Calculadora.calcular(-2,-3,'*')
        self.assertEqual(resultado, 6)


class TestDivisao(TestCase):
    def test_divisao_comum(self):
        resultado = Calculadora.calcular(4,2,'/')
        self.assertEqual(resultado, 2)

    def test_divisao_negativos(self):
        resultado = Calculadora.calcular(-10, -2,'/')
        self.assertEqual(resultado, 5)

    def test_divisao_quebrada(self):
        resultado = Calculadora.calcular(10, 3,'/')
        self.assertEqual(resultado, 3.3333333333333335)

    def test_divisao_por_zero(self):
        resultado = Calculadora.calcular(2, 0, '/')
        self.assertEqual(resultado, 'Erro: Impossível dividir por 0')

#print('* Exemplo: 2 * 3 =', Calculadora.calcular(2,3,'*'))

if _name_ == '_main_':
    main(verbosity=2)
