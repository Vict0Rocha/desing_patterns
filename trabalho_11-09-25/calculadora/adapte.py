"""
Adapta as classes Subtracao, Multiplicacao e Divisao para a interface comum Operacao.
"""

from abc import ABC, abstractmethod

# Interface comum para operações
class Operacao(ABC):
    @abstractmethod
    def executar(self, a, b):
        pass

# Implementação padrão de soma
class Soma(Operacao):
    def executar(self, a, b):
        return a + b

# Implementação de subtração que queremos adaptar
class Subtracao:
    def subtrair(self, x, y):
        return x - y

# Adapter para SubtracaoAPI
class SubtracaoAdapter(Operacao):
    def __init__(self, subtrair):
        self.subtrair = subtrair
    def executar(self, a, b):
        return self.subtrair.subtrair(a, b)

# Implementação de multiplicação que queremos adaptar
class Multiplicacao:
    def multiplicar(self, x, y):
        return x * y
    
# Adapter para Multiplicacao
class MultiplicacaoAdapter(Operacao):
    def __init__(self, multiplicar):
        self.multiplicar = multiplicar
    def executar(self, a, b):
        return self.multiplicar.multiplicar(a, b)

# Implementação de divisão que queremos adaptar
class Divisao:
    def dividir(self, x, y):
        if y == 0:
            raise ValueError("Divisão por zero não é permitida.")
        return x / y
# Adapter para Divisao
class DivisaoAdapter(Operacao):
    def __init__(self, dividir):
        self.dividir = dividir
    def executar(self, a, b):
        return self.dividir.dividir(a, b)


if __name__ == "__main__":
    soma = Soma()
    subtracao = SubtracaoAdapter(Subtracao())
    print("Soma:", soma.executar(10, 5))
    print("Subtração:", subtracao.executar(10, 5))
