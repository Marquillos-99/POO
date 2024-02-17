"""
Clase padre = Comida
Clase Fruta hereda de Clase comida
Clase postre hereda de clase  comida
"""
class Comida:
    def __init__(self,nombre,sabor):
        self.nombre = nombre
        self.sabor = sabor

    def describe(self):
        return f"{self.nombre} tiene sabor {self.sabor}"
    
class Fruta(Comida):
    def __init__(self,nombre,sabor,color):
        super().__init__(nombre,sabor)
        self.color = color
        
    def describe(self):
        return f"{self.nombre} es una fruta de color {self.color} y tiene sabor {self.sabor}"
    
class Postre(Comida):
    def __init__(self,nombre,sabor,dulzura):
        super().__init__(nombre,sabor)
        self.dulzura = dulzura

    def describe(self):
        return "{} es un postre dulce con sabor {} y nivel de dulzura {}".format(self.nombre,self.sabor,self.dulzura)
    

manzana = Fruta("Manzana","dulce","roja")
pastel_chocolate = Postre("Pastel Chocolate","rico","alta")

print(manzana.describe())
print(pastel_chocolate.describe())