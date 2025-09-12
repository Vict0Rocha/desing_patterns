"""
Factory Method para operações matemáticas usando Adapter.
Retorna instâncias das operações adaptadas para interface comum.
"""

from adapte import Soma, SubtracaoAdapter, MultiplicacaoAdapter, DivisaoAdapter, Subtracao, Multiplicacao, Divisao

class OperacaoFactory:
    @staticmethod
    def criar_operacao(tipo):
        if tipo == 'soma':
            return Soma()
        elif tipo == 'subtracao':
            return SubtracaoAdapter(Subtracao())
        elif tipo == 'multiplicacao':
            return MultiplicacaoAdapter(Multiplicacao())
        elif tipo == 'divisao':
            return DivisaoAdapter(Divisao())
        else:
            raise ValueError(f"Operação '{tipo}' não suportada.")

# Calculadora concreta usando Factory e Adapter
class Calculadora:
    def soma(self, a, b):
        return OperacaoFactory.criar_operacao('soma').executar(a, b)

    def sub(self, a, b):
        return OperacaoFactory.criar_operacao('subtracao').executar(a, b)

    def mult(self, a, b):
        return OperacaoFactory.criar_operacao('multiplicacao').executar(a, b)

    def div(self, a, b):
        return OperacaoFactory.criar_operacao('divisao').executar(a, b)