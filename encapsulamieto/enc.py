class Ejemplo:
    def publico(self):
        print("publico")

    def __privado(self):
        print("privado")
    
    def getPrivado(self):
        vor=self.__privado
        print(vor)
    

    

    
ej = Ejemplo()
ej.publico()
ej.getPrivado()

# _ClASE__ObJPriva
#