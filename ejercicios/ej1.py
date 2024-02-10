class Persona():

    def __init__(self,name,age,dni):
        self.name = name
        self.age = age
        self.dni = dni

    @property
    def name(self):
        return self.__name
    
    @property
    def age(self):
        return self.__age
    
    @property
    def dni(self):
        return self.__dni
    
    @name.setter
    def name(self,name):
        self.__name = name

    def validar_dni(self):
        letters = "TRWAGMYFPDXBNJZSQVHLCKE"

        if len(self.__dni) !=9:
            print("CURP incorrecto")
            self.__dni = ""
        else:
            letters = self.__dni[8]
            num = int(self.__dni[:8])
            if letters.upper() != letters[num % 23]:
                print("DNI incorrecto")
                self.__dni = ""

    @dni.setter
    def dni(self,dni):
        self.__dni = dni
        self.validar_dni()

    @age.setter
    def age(self,age):
        if age<0:
            print("Edad incorrecta")
            self.__age = 0
        else:
            self.__age = age

    def show(self):
        return f"Mi nombre es {self.name} - Edad:{self.age} - CURP:{self.dni}"
    
    def esMayorDeEdad(self):
        return self.age>=18
    
juan = Persona("juan",20,"TRNENENE5O",)
print(juan)