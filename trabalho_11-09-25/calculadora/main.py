
from factory import Calculadora
from singleton import AppSettings

if __name__ == "__main__":
    calc = Calculadora()
    settings = AppSettings()

    a, b = 10, 5
    print(f'Soma: {calc.soma(a, b)}')
    print(f'Subtração: {calc.sub(a, b)}')
    print(f'Multiplicação: {calc.mult(a, b)}')
    print(f'Divisão: {calc.div(a, b)}')

    settings.salvar(f'Soma de {a} e {b}: {calc.soma(a, b)}')
    settings.salvar(f'Subtração de {a} e {b}: {calc.sub(a, b)}')
    settings.salvar(f'Multiplicação de {a} e {b}: {calc.mult(a, b)}')
    settings.salvar(f'Divisão de {a} e {b}: {calc.div(a, b)}')

    print('\nHistórico de operações:')
    settings.mostrarHistorico()