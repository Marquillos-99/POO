class Deportista:
    def __init__(self,genero, edad, peso):
        self.genero = genero
        self.edad = edad        
        self.peso = peso

    def __str__(self):
        return(f"Mi genero es: {self.genero}, mi edad: {self.edad} y peso es: {self.peso}")

class Ciclista(Deportista):
    def __init__(self,genero,edad,peso,name):
        super().__init__(genero,edad,peso)
        self.name = name


    def __str__(self):
        return Deportista.__str__(self)+ f" ademas mi nombre es {self.name}"
    

deporte = Ciclista("hombre",17,60,"Toto")
print(deporte)