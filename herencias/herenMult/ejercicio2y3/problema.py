class Cuenta():
    def __init__(self,titular,cantidad = 0):
        self.titular = titular
        self.cantidad = cantidad

    @property 
    def titular(self):
        return self.__titular
    
    @property 
    def cantidad(self):
        return self.__cantidad
    
    @titular.setter
    def titular(self,new_titular):
        self.__titular = new_titular

    @cantidad.setter
    def cantidad(self,new_cantidad):
        self.__cantidad = new_cantidad

    def mostrar(self):
        return f"Cuenta \n Titular:{self.titular.mostrar()} - Cantidad:{self.cantidad}"
    
    def ingresar(self,cantidad):
        if cantidad>0:
            self.cantidad += cantidad

    def retirar(self,cantidad):
        if cantidad > 0:
            self.cantidad -= cantidad
