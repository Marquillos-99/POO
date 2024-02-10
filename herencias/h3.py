class Persona():
    def __init__(self,apepat,apemat, name):
        self.ApellidoPat = apepat
        self.ApellidoMat = apemat
        self.Name = name

    def mostrarNombreCompleto(self):
        return 'Mi primer apellido es {} mi segundo apellido es {} y mi nombre es {}'.format(self.ApellidoPat, self.ApellidoMat, self.Name)

class Estudiante(Persona):
    def __init__(self, apepat, apemat, name):
        super().__init__(apepat, apemat, name)


est1 = Estudiante("Alvarado","Bringas","Marcos")

print(est1.mostrarNombreCompleto())