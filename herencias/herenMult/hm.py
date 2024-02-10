class Terrestre:
    def desplazalse(self):
        print("El animal anda")

class Acuatico:
    def desplazalse(self):
        print("El animal nada")

class Cocodrilo(Terrestre,Acuatico):
    pass

c = Cocodrilo()
c.desplazalse