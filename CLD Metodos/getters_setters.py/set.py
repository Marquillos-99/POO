class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def set_edad(self, new_edad):
        self.edad = new_edad

    
persona1 = Persona("Ana",25)
persona1.set_edad(30)

print(persona1.edad)
