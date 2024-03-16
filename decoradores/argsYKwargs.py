def decorator(funcion):
    def wrapper(*args, **kwargs):
        print('Antes de la funcion')
        funcion(*args, **kwargs)
        print('Despues de la funcion')
    return wrapper

@decorator
def saludo():
    print("Hola Mundo ")

saludo()