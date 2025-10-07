from time import sleep
from abc import ABC, abstractmethod

class Image(ABC):
    @abstractmethod
    def load(self): pass

class RealImage(Image):
    def __init__(self, file_name) -> None:
        self.file_name = file_name
        self._is_load = False

    def load(self):
        if self._is_load:
            print(f'Carregando {self.file_name}')
            return

        print(f'Carregando {self.file_name}...')
        sleep(4)
        print(f'{self.file_name} carregado com [SECESSO]')
        self._is_load = True

class ProxyImage(Image):
    def __init__(self, file_name) -> None:
        self.file_name = file_name
        self.real_object = None

    def load(self):
        if self.real_object is None:
            self.real_object = RealImage(self.file_name)

        self.real_object.load()

if __name__ == '__main__':
    imagem1 = ProxyImage('Aula proxy')
    imagem1.load()
    imagem1.load()
    imagem1.load()
    imagem1.load()
