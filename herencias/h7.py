class Vehiculo:
    def __init__(self,limite):
        self.velocidadlimite=limite
    def encender(self):
        print("El vehiculo encendio")
    def velocidadMax(self):
        print(self.velocidadlimite)

class Auto(Vehiculo):
    def __init__(self,marca,modelo,velocidad):
        super().__init__(velocidad)
        self.marca=marca
        self.modelo=modelo
    def quesoy(self):
        print("Soy un auto")
    
class Moto(Vehiculo):
    def __init__(self,marca,modelo,velocidad):
        self.marca=marca
        self.modelo=modelo
        super().__init__(velocidad)
    def quesoy(self):
        print("Soy una moto")

Pulsar=Moto("Honda","2020","300")
Tsuru=Auto("Nisan","2007","120")

Pulsar.encender()
Tsuru.encender()

Pulsar.velocidadMax()
Pulsar.quesoy()

Tsuru.velocidadMax()
Tsuru.quesoy()