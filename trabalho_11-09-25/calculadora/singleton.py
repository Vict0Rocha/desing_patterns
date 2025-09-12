class AppSettings:
    _instance = None

    def __new__(cls, *args,**kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self) -> None:
        # O inicializador é executado todas as vezes.
        print('inicializando...')
        self.tema = 'escuro'
        self.historico = []

    def salvar(self, operacao):
        self.historico.append(operacao)

    def mostrarHistorico(self):
        for conteudo in self.historico:
            print(conteudo)