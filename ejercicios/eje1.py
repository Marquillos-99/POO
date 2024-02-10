class Persona:
    def __init__(self, name, age, dni):
        self._name = name
        self._age = age
        self._dni = dni

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def dni(self):
        return self._dni

    @name.setter
    def name(self, name):
        self._name = name

    def validar_dni(self):  # Review and adjust validation logic as needed
        letters = "TRWAGMYFPDXBNJZSQVHLCKE"

        if len(self._dni) != 9:
            print("CURP incorrecto")
            self._dni = ""
        else:
            letters = self._dni[8]
            num = int(self._dni[:8])
            if letters.upper() != letters[num % 23]:
                print("DNI incorrecto")
                self._dni = ""

    @dni.setter
    def dni(self, dni):
        self._dni = dni
        self.validar_dni()

    @age.setter
    def age(self, age):
        if age < 0:
            print("Edad incorrecta")
            self._age = 0
        else:
            self._age = age

    def show(self):
        return f"Mi nombre es {self.name} - Edad:{self.age} - CURP:{self.dni}"

    def esMayorDeEdad(self):
        return self.age >= 18

juan = Persona("Juan", 20, "TRWAGMYFPDXBNJZSQVHLCKE")
print(juan)