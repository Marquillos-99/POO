#class

class Auto:
    #versiones de python 3 y anteriores ==> class Auto(object)
    marca = ""
    modelo = 0
    placa = ""

taxi = Auto()
#Jala?
#Para un dato le pasas el objeto y el atributo que deses obtener
print(Auto.modelo)

"""crea una clase llamada Persona con atributos ==> doctor, bombero, electricista

**crea una clase de Jugadores_A y Jugadores_B como atributo pasale al menos 2 jugadores a cada uno
  e imprime tus resultados para comprobar que es correcto
"""
#si no quieres usar una clase en ese instante

class Superheroes:
    pass

captainAmerica = Superheroes()
ironMan = Superheroes()
blackWidow = Superheroes()

#objeto.atributo = valor (el atributo NECESITA un valor)

captainAmerica.escudo = True
captainAmerica.traje = True
captainAmerica.esElTraseroDeAmerica = "Si"
#----------------- ----------------------- --------------------
ironMan.sexo = "Masculino"
ironMan.masFuerteQueElCap = False
ironMan.pais = 'USA'
#--------------- --------------------- --------------------
blackWidow.pais = 'Rusa'
blackWidow.sexo = "Femenino"

print ("El cap tiene escudo?")
print(captainAmerica.escudo)

