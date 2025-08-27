def singleton (the_class):
    instance = {}

    def get_class(*args, **kwargs):
        if the_class not in instance:
            instance[the_class] = the_class(*args, **kwargs)
        return instance[the_class]

    return get_class

@singleton
class AppSettings:
    def __init__(self):
        # O inicializador é executado apenas uma vez.
        print('inicializando...')
        self.tema = 'Escuro'
        self.font = '18px'

if __name__ == '__main__':
    as1 = AppSettings()
    as2 = AppSettings()
    
    print(as1 == as2)
    print(as1.tema)
    as1.tema = 'claro'
    print(as1.tema)

    as3 = AppSettings()
    print(as3.tema)