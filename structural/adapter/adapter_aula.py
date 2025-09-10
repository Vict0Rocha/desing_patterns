class AntigaEmpresa:
    def factorial(self):
        print('ANTIGO fatorial')

    def verifica_maior(self):
        print('ANTIGO verifica maior')

class NovaEmpresa:
    def f(self):
        print('NOVA fatorial')

    def vm(self):
        print('NOVA verifica maior')

class AdaptadorCalculadora(AntigaEmpresa):
    def __init__(self, n_calculadora: NovaEmpresa):
        self.n_calculadora = n_calculadora

    def factorial(self):
        self.n_calculadora.f()

    def verifica_maior(self):
        self.n_calculadora.vm()

nova_empresa = NovaEmpresa()
calculadora = AdaptadorCalculadora(nova_empresa)
# print(calculadora.factorial())

calculadora.factorial()

# def teste():
#     print('teste')

# print(teste())