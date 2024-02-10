class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f"El color es {self.color}, tiene {self.ruedas} ruedas"

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + f" {self.velocidad} km/h, cc {self.cilindrada}"

class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return super().__str__() + f" {self.carga} kg"
    

coche = Coche("azul", 4, 150, 1200)
print(coche)