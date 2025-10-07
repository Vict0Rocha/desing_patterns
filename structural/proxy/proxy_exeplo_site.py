"""
O Proxy é um padrão de projeto estrutural que tem a
intenção de fornecer um objeto substituto que atua
como se fosse o objeto real que o código cliente
gostaria de usar.
O proxy receberá as solicitações e terá controle
sobre como e quando repassar tais solicitações ao
objeto real.

Com base no modo como o proxies são usados,
nós os classificamos como:

- Proxy Virtual: controla acesso a recursos que podem
ser caros para criação ou utilização.
- Proxy Remoto: controla acesso a recursos que estão
em servidores remotos.
- Proxy de proteção: controla acesso a recursos que
possam necessitar autenticação ou permissão.
- Proxy inteligente: além de controlar acesso ao
objeto real, também executa tarefas adicionais para
saber quando e como executar determinadas ações.

Proxies podem fazer várias coisas diferentes:
criar logs, autenticar usuários, distribuir serviços,
criar cache, criar e destruir objetos, adiar execuções
e muito mais...
"""

# from __future__ import annotations
from abc import ABC, abstractmethod
from time import sleep
from typing import List, Dict


class IUsuario(ABC):
    """ Subject Interface """

    @abstractmethod
    def pega_endereco(self) -> List[Dict]: pass

    @abstractmethod
    def pega_dados_usuarios(self) -> Dict: pass

class UsuarioReal(IUsuario):
    """ Real Subject """

    def __init__(self, primeiro_nome: str, segundo_nome: str) -> None:
        sleep(2) # Simulando uma requisição
        self.primeiro_nome = primeiro_nome
        self.segundo_nome = segundo_nome


    def pega_endereco(self) -> List[Dict]: 
        sleep(2) # Simulando uma requisição
        return [
            {'avenida': 'brasil', 'numero': '01010'}
        ]

    def pega_dados_usuarios(self) -> Dict: 
        sleep(2) # Simulando uma requisição
        return {
            'cpf': '111.111.111-11',
            'rg': 'AB123456'
        }
    
class Proxy(IUsuario):
    """ Proxy """
    def __init__(self, primeiro_nome: str, segundo_nome: str) -> None:
        self.primeiro_nome = primeiro_nome
        self.segundo_nome = segundo_nome

        # Esses objetos nesse ponto do código ainda não existem
        self._usuario_real: UsuarioReal
        self._cache_endereco: List[Dict]
        self._dados_usuarios: Dict

    def pega_usuario_real(self) -> None:
        if not hasattr(self, '_usuario_real'):
            self._usuario_real = UsuarioReal(self.primeiro_nome, self.segundo_nome)

    def pega_endereco(self) -> List[Dict]: 
        self.pega_usuario_real()

        if not hasattr(self, '_cache_endereco'):    
            self._cache_endereco = self._usuario_real.pega_endereco()
        
        return self._cache_endereco
        
    def pega_dados_usuarios(self) -> Dict: 
        self.pega_usuario_real()

        if not hasattr(self, '_dados_usuarios'):    
            self._dados_usuarios = self._usuario_real.pega_dados_usuarios()
        
        return self._dados_usuarios

if __name__ == '__main__':
    usuario1 = Proxy('Victor', 'Hugo')

    # Responde instantaneamente
    print(usuario1.primeiro_nome)
    print(usuario1.segundo_nome)

    # 6 segundos para obter resposta
    print(usuario1.pega_dados_usuarios())
    print(usuario1.pega_endereco())

    # Aqui é respondido instantaneamente
    print('DADOS EM CACHE')
    for i in range(5):
        print(usuario1.pega_endereco())
        print(usuario1.pega_dados_usuarios())

    """
    O Proxy vai ter os mesmos metodos do objeto real. Porque ele implementa
    a mesma interface. O proxy vai manter uma ligação com o objeto real,
    "Ele conhece o objeto", e pode manter o objeto real dentro do seu codigo. 
    """
