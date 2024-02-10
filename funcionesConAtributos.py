#funciones con atributos 

class Persona:
    edad = 27
    nombre = "Juan"
    pais = "Mexico"

programador = Persona()

#print('La edad del programador es de ',programador.edad," años")

# Atributos -> vamos a poder sacar provecho con algunas palabras reservadas

#print('la edad es: ', getattr(programador,"nombre"))

#print("el programador tiene una edad?", hasattr(programador,"edad"))

#hasattr(object, name) revisa si existe algun atributo con ese nombre regresando un valor booleano

"""print(programador.nombre)
setattr(programador,"nombre", "david")
print(programador.nombre)
"""
#setattr modifica el valor de un objeto setattr(programador, edad, 30)

"""
delattr(Persona, 'pais')
print(programador.nombre,' ', programador.edad)
print(programador.pais)
"""

#delattr(object , name) de la CLASE

