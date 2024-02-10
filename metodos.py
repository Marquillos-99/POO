"""un metodo lo que hace es determinar una accion o un comportamiento
*** como escribo un metodo?
*** class nombre de la clase 
*** palabra reservada DEF nombre del metodo (usamos def para saber que estamos haciendo un metodo)
*** palabra reservada SELF (self): lo que hace es referirse al objeto en si mismo

*** Self.nombre de la variable = Algoritmo
ejecuta el metodo con el valor dado
"""

class Mates:
    def suma(self):
        self.n1 = 2 #asignamos variables
        self.n2 = 4

Adicion = Mates()

#Que elemento va a llamar ese metodo ==> El Objeto
Adicion.suma() 
#ejecutar el metodo
print(Adicion.n1 + Adicion.n2)

#metodo con init ==> ___init___(SEFT)
#gracias a este init vamos a poder realizar cualquier tipo de trabajo con cualquier objeto/propiedad

class Ropa:
    def __init__(self):
        self.marca = "Puma" #asignamos atributos
        self.talla = "M"
        self.color = "rojo"

Hoddie = Ropa()
print(Hoddie.talla)

""" Crea una clase que se llame Calculadora que tenga una suma, resta, multiplicacion y division
    con objeto 'Operacion'
"""

class Calculadora:
    def __init__(self,n1,n2):
        self.suma = n1 + n2
        self.resta = n1 + n2
        self.multiplicacion = n1 + n2
        self.division = n1 + n2

Operacion = Calculadora(5,2)
print(Operacion.multiplicacion)

# con que variables trabaja el metodo?
