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
    
class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas,urbana,deportiva):
        super().__init__(color, ruedas)
        self.urbana = urbana
        self.deportiva = deportiva

    def __str__(self):
        return f"Bicicleta: {self.color}, {self.ruedas} ruedas. Urbana: {self.urbana}, Deportiva: {self.deportiva}"



    

coche = Bicicleta("azul", 2, True, False)
print(coche)