from abc import ABC, abstractmethod

# --- 1. Padrão Singleton 
def singleton(a_classe):
    instancias = {}
    def obter_instancia(*args, **kwargs):
        if a_classe not in instancias:
            instancias[a_classe] = a_classe(*args, **kwargs)
        return instancias[a_classe]
    return obter_instancia

@singleton
class AppSettings:
    def __init__(self):
        print('>>> Configurações da aplicação inicializadas (Singleton)...')
        self.tema = 'Escuro'

# --- 2. Padrão Adapter

class ICalculadora(ABC):
    @abstractmethod
    def soma(self): pass

    @abstractmethod
    def sub(self): pass

class CalculadoraAntiga:
    def adicao(self):
        print('Calculadora ANTIGA: Executando método de adição...')
    
    def subtracao(self):
        print('Calculadora ANTIGA: Executando método de subtração...')

class AdaptadorCalculadoraAntiga(ICalculadora):
    def __init__(self):
        self._calculadora_antiga = CalculadoraAntiga()

    def soma(self):
        self._calculadora_antiga.adicao()
    
    def sub(self):
        self._calculadora_antiga.subtracao()

# --- 3. Padrão Factory Method 
class FabricaDeCalculadora:
    def criar_calculadora(self) -> ICalculadora:
        print("FÁBRICA: Criando a calculadora para o cliente...")
        return AdaptadorCalculadoraAntiga()

def main():
    print("--- Calculadora com Fábrica Simples, Adapter e Singleton ---")

    config = AppSettings()
    print(f"Tema da aplicação: {config.tema}\n")
    
    fabrica = FabricaDeCalculadora()
    calculadora = fabrica.criar_calculadora()
    
    print("\nCLIENTE: Usando a calculadora recebida da fábrica...")
    calculadora.soma()
    calculadora.sub()
    
    print("\nO cliente usou a calculadora sem nunca saber que era um sistema antigo e adaptado!")

if __name__ == "__main__":
    main()