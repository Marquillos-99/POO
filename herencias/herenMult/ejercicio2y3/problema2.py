from problema import Cuenta

class CuentaJoven(Cuenta):
    def __init__(self,titular,cantidad = 0, bonificion = 0,edad = 0):
        super().__init__(titular,cantidad)
        self.bonificion = bonificion
        self.edad = edad

    @property
    def bonificion(self):
        return self.__bonificion
    
    @bonificion.setter
    def bonificion(self,bonificion):
        self.__bonificion = bonificion
    
    def mostrar(self):
        return "Cuenta Joven\n" + "Titular:" + self.titular.mostrar()+ " -Cantidad:"+str(self.cantidad)+"Bonificion:"+str(self.bonificion)
    
    def esTitularValido(self):
        return self.edad < 25 and self.esMayorDeEdad
    
    def retirar(self, cantidad):
        if not self.esTitularValido():
            print('no puedes retirar dinero')
        elif cantidad > 0:
            super().retirar(cantidad)

#Crear una persona
juan = Cuenta("juan",28)

#creamos cuenta para joven
cuenta_joven_juan = CuentaJoven("juan", 1000, 5, 28)

#cuenta normal
cuenta_ana = Cuenta("Ana",500)


print(cuenta_joven_juan.titular)
print(cuenta_joven_juan.edad)
cuenta_joven_juan.titular = "pedro"
print(cuenta_joven_juan.titular)
cuenta_joven_juan.bonificion = 10
print(cuenta_joven_juan.bonificion)

cuenta_joven_juan.retirar(300)
print(cuenta_joven_juan.cantidad)
