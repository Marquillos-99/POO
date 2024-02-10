class Calculadora:
    def __init__(self, numbers2,):
        self.numbers = numbers2
        self.data = [ 0 for i in range(numbers2)]
#si necesito 2 n o 1 se hace con bucles
        
    def DataIn(self):
        self.data = [int(input('ingresar datos '+ str(i+1)+' = ')) for i in range(self.numbers)]
        #para llamar por consola

class Operations(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,2)
        #limitas los atributos que necesitas

    def suma(self):
        #self.data = a,b
        a,b = self.data
        suma = a + b
        print('el resultado es: ', suma)

    def resta(self):
        #self.data = a,b
        a,b = self.data
        resta = a - b
        print('el resultado es: ', resta)

    def multiplicacion(self):
        #self.data = a,b
        a,b = self.data
        multiplicacion = a * b
        print('el resultado es: ', multiplicacion)

    def division(self):
        #self.data = a,b
        a,b = self.data
        division = a / b
        print('el resultado es: ', division)

class raiz(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,1)

    def raizCuadrada(self):
        import math
        a, = self.data
        print('El resultado es: ',math.sqrt(a))

ejemplo=raiz()
print(ejemplo.DataIn())
print(ejemplo.raizCuadrada())