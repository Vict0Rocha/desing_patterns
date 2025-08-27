from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def busca_cliente(self) -> None: pass


class CarroLuxo(Veiculo):
    def busca_cliente(self) -> None:
        print('Carro LUXO está buscando cliente...')

class CarroPopular(Veiculo):
    def busca_cliente(self) -> None:   
        print('Carro POPULAR está buscando cliente...')

class VeiculoFactory:
    def __init__(self, tipo):
        self.carro = self.get_carro(tipo)

    @staticmethod
    def get_carro(tipo: str) -> Veiculo: #type: ignore 
        if tipo == 'luxo':
            return CarroLuxo()
        if tipo == 'popular':
            return CarroPopular()
        assert 0, 'Veiculo não existe!'

    def busca_cliente(self):
        self.carro.busca_cliente()

if __name__ == '__main__':
    from random import choice

    carros_disponiveis = ['luxo', 'popular']

    for i in range(5):
        carro = VeiculoFactory(choice(carros_disponiveis))
        carro.busca_cliente()

"""
Nesse caso:
O cliente instancia a factory direto.
Cliente pedi a factory para usar algum metodo dentro do produto.
'A minha factory envolve o meu objeto.'
"""