class Decorator(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Antes de la llamada')
        retorno = self.func(*args, **kwargs)
        print('Despues de la llamada')
        print(retorno)
        return retorno
    

@Decorator
def func():
    print('Dentro de la Funcion')
    return "Returno"

func()

