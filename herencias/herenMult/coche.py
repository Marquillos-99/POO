class Vehiculo:
    def __init__(self,marca):
        self.marca=marca

    def describe(self):
        return f"Este vehiculo es de la marca {self.marca}"


class Motorizado:
    def arrancar(self):
        return f"Este vehiculo esta encendido"
    

class Electrico:
    def carga(self):
        return f"Este vehiculo esta cargando"


class Coche(Vehiculo,Motorizado,Electrico):
    def __init__(self,marca,modelo):
        super().__init__(marca)
        self.modelo = modelo
    
    def describe(self):
        return f"Este coche {self.marca} {self.modelo} es motorizado y elecrico"
    

carro = Coche("Tesla","Model 3")

print(carro.describe())
print(carro.arrancar())
print(carro.carga())