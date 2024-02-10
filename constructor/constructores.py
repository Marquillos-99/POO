"""los metodos en una clase comienzan con __

__init__()
"""

'''
class Persona:
    pass
    def __init__(self, name, years):
        self.name = name
        self.years = years
    
    def descripcion(self):
        return '{} has {} years old'.format(self.name, self.years)
    
    def comentario(self,frase):
        return '{} dice: {}'.format(self.name, frase)
    
programador = Persona("Marcos","25")
print(programador.descripcion())
print(programador.comentario('Si el codigo funciona, No lo toques'))
'''

#traigo una funcion, .format para que funcione necesito pasarle parametros en las comillas
    #lo que hara que le pase los parametros al return