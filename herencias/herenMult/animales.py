'''
Clase padre = Animal
Clase Volador hereda de clase Animal
Clase Nadador hereda de clase Animal
Clase Ave hereda de clase Animal y volador
Clase Pez hereda de clase Animal y nadador
'''

class Animal:
    def __init__(self,nombre):
        self.nombre = nombre

    def describe(self):
        print(f'Este animal se llama {self.nombre}')

class Volador(Animal):
    def volar(self):
        return "Este animal puede Volar"
    
class Nadador(Animal):
    def nadar(self):
        return "Este animal puede Nadar"
    
class Ave(Volador,Animal):
    def __init__(self, nombre,especie):
        super().__init__(nombre)
        self.especie = especie
        
    def describe(self):
        return f"Este ave {self.nombre} es de la especie {self.especie} y puede volar"
    
class Pez(Nadador,Animal):
    def __init__(self, nombre,tipo):
        super().__init__(nombre)
        self.tipo = tipo

    def describe(self):
        return f"Este pez {self.nombre} es de tipo {self.tipo} y puede nadar"
    
aguila = Ave("Aguila","Rapaz")
tiburon = Pez("Tiburon","Martillo")

print(aguila.describe())
print(aguila.volar())

print(tiburon.describe())

print(tiburon.nadar())