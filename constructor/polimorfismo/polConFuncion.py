class Tomate:
    def tipo(self):
        print('vegetal')

    def color(self):
        print('verde')

class Manzana:
    def tipo(self):
        print('fruta')

    def color(self):
        print('rojo')


def funcion(object):
    object.tipo()
    object.color()

new_tomate = Tomate()
funcion(new_tomate)

new_apple = Manzana()
funcion(new_apple)