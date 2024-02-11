class Clase:
    atributo_clase = "Hola"
    __atributo_clase2 = "Hola"

    def __init__(self,atributo_instancia):
        self.atributo_instancia = atributo_instancia

    def __mi_metodo(self):
        print("Haz algo")
        self.__variable = 0

    def metodo_normal(self):
        self.__mi_metodo()

mi_clase = Clase("Que onda")
mi_clase.atributo_clase
mi_clase.metodo_normal()


print(dir(mi_clase))

#como puedo acceder a los atributos privados

#1
class Miclass:
    def __init__(self):
        pass

