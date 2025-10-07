from time import sleep
from abc import ABC, abstractmethod
from typing import Dict


class IUser(ABC):
    @abstractmethod
    def pega_dados_usuarios(self) -> Dict: pass

class RealUser(IUser):
    def __init__(self, name: str) -> None:
        sleep(2) # Simulando uma requisição no BD
        self.name = name

    def pega_dados_usuarios(self) -> Dict:
        sleep(4) # Simulando uma requisição
        return {
            'cpf':'123.456.789-01',
            'rg':'ABC123-9',
        }
    
class UserProxy(IUser):
    def __init__(self, name: str) -> None:
        self.name = name

        self._real_user: RealUser
        self._cache_address: Dict

    def get_real_user(self) -> None:
        if not hasattr(self, '_real_user'):
            self._real_user = RealUser(self.name)

    def pega_dados_usuarios(self) -> Dict:
        self.get_real_user()

        if not hasattr(self, '_cache_address'):
            self._cache_address = self._real_user.pega_dados_usuarios()

        return self._cache_address
    
if __name__ == '__main__':
    user = UserProxy('Hugo')

    print(user.name)

    print(user.pega_dados_usuarios())
    print(user.pega_dados_usuarios())
    print(user.pega_dados_usuarios())
    print(user.pega_dados_usuarios())
    print(user.pega_dados_usuarios())
    print(user.pega_dados_usuarios())