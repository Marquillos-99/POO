class Persona:
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad

personas = [Persona("Juan", 20), Persona("Pedro", 30), Persona("Maria", 40)]

edades = map(lambda persona: persona.nombre, personas)
edadfinal = list(edades)

print(edadfinal)