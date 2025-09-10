"""
Adapter é um padrão de projeto estrutural que
tem a intenção de permitir que duas classes
que seriam incompatíveis trabalhem em conjunto
através de um "adaptador".
"""

from abc import ABC, abstractmethod

class IControle(ABC):
    @abstractmethod
    def cima(self): pass
    
    @abstractmethod
    def baixo(self): pass
    
    @abstractmethod
    def direita(self): pass
    
    @abstractmethod
    def esquerda(self): pass

class Controle(IControle):
    def cima(self): 
        print('Movendo para CIMA')
    
    def baixo(self): 
        print('Movendo para BAIXO')
    
    def direita(self): 
        print('Movendo para DIREIRA')
    
    def esquerda(self):
        print('Movendo para ESQUERDA')

class NovoControle():
    def move_cima(self): 
        print('NOVO CONTROLE: Movendo para CIMA')
    
    def move_baixo(self): 
        print('NOVO CONTROLE: Movendo para BAIXO')
    
    def move_direita(self): 
        print('NOVO CONTROLE: Movendo para DIREIRA')
    
    def move_esquerda(self):
        print('NOVO CONTROLE: Movendo para ESQUERDA')

class AdpaterControle(): 
    """ Adapter Object """

    def __init__(self, novo_controle: NovoControle) -> None:
        self.novo_controle = novo_controle

    def cima(self): 
        self.novo_controle.move_cima()        

    def baixo(self): 
        self.novo_controle.move_baixo()        

    def direita(self): 
        self.novo_controle.move_direita()        

    def esquerda(self):
        self.novo_controle.move_esquerda()        

class AdpaterControle2(Controle, NovoControle):
    """ Adapter Class """

    def cima(self): 
        self.move_cima()        

    def baixo(self): 
        self.move_baixo()        

    def direita(self): 
        self.move_direita()        

    def esquerda(self):
        self.move_esquerda() 

if __name__ == "__main__":

    # Controle - Apdater Object

    novo_controle = NovoControle()
    controle_object = AdpaterControle(novo_controle)
    controle_object.cima()
    controle_object.baixo()
    controle_object.direita()
    controle_object.esquerda()

    print()

    # Controle - Apdater class

    controle_object = AdpaterControle2()
    controle_object.cima()
    controle_object.baixo()
    controle_object.direita()
    controle_object.esquerda()