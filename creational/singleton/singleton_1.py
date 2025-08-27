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
    
if __name__ == "__main__":
    as1 = AppSettings()
    as2 = AppSettings()

    print(as1 == as2)
    as1.tema = 'claro'
    print(as1.tema)

    as3 = AppSettings()
    print(as1.tema)