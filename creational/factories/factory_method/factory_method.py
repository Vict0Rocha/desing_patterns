"""
Factory method é um padrão de criação que permite definir uma interface para
criar objetos, mas deixa as subclasses decidirem quais objetos criar. O
Factory method permite adiar a instanciação para as subclasses, garantindo o
baixo acoplamento entre classes.
"""

from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def busca_cliente(self) -> None: pass


class CarroLuxo(Veiculo):
    def busca_cliente(self) -> None:
        print('CARRO LUXO está buscando cliente...')

class CarroPopular(Veiculo):
    def busca_cliente(self) -> None:   
        print('CARRO POPULAR está buscando cliente...')

class MotoPopular(Veiculo):
    def busca_cliente(self) -> None:   
        print('MOTO POPULAR está buscando cliente...')

class MotoLuxo(Veiculo):
    def busca_cliente(self) -> None:   
        print('MOTO LUXO está buscando cliente...')

class VeiculoFactory(ABC):
    def __init__(self, tipo) -> None:
        self.carro = self.get_carro(tipo)

    @staticmethod
    @abstractmethod
    def get_carro(tipo: str) -> Veiculo: pass 

    def busca_cliente(self):
        self.carro.busca_cliente()

class ZonaNorteVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo: #type: ignore 
        if tipo == 'carro_luxo':
            return CarroLuxo()
        if tipo == 'carro_popular':
            return CarroPopular()
        if tipo == 'moto_popular':
            return MotoPopular()
        if tipo == 'moto_luxo':
            return MotoLuxo()
        assert 0, 'Veiculo não existe!'

class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo: #type: ignore 
        if tipo == 'carro_popular':
            return CarroPopular()
        assert 0, 'Veiculo não existe!'

if __name__ == '__main__':
    from random import choice

    veiculos_disponiveis_zona_norte = ['carro_luxo', 'carro_popular', 'moto_popular', 'moto_luxo']
    veiculos_disponiveis_zona_sul = ['carro_popular']

    print('ZONA NORTE')
    for i in range(5):
        carro1 = ZonaNorteVeiculoFactory(choice(veiculos_disponiveis_zona_norte))
        carro1.busca_cliente()

    print('ZONA SUL')
    for i in range(5):
        carro2 = ZonaSulVeiculoFactory(choice(veiculos_disponiveis_zona_sul))
        carro2.busca_cliente()
        