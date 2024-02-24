class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def get_name(self):
        return self.nombre
    
    def get_edad(self):
        return self.edad
    
persona1 = Persona("Ana",25)
nombre = persona1.get_name()
edad = persona1.get_edad()
print(nombre)
print(edad)
