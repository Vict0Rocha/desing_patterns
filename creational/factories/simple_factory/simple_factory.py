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
    @staticmethod
    def get_carro(tipo: str) -> Veiculo: #type: ignore 
        if tipo == 'luxo':
            return CarroLuxo()
        if tipo == 'popular':
            return CarroPopular()
        assert 0, 'Veiculo não existe!'

if __name__ == '__main__':
    from random import choice

    carros_disponiveis = ['luxo', 'popular']

    for i in range(10):
        carro = VeiculoFactory.get_carro(choice(carros_disponiveis))
        carro.busca_cliente()

"""
Nesse caso:
O cliente pedi a factory.
A factory cria o objeto.
O cliente usa o objeto.
"""