#herencia es crear una nueva clase a partir de una o mas clases existentes

'''

class SubClaseName(SupClaseName)

class BaseClass:
        Body Base Class

class DerivadoClase(BaseClass)
        Cuerpo Clase Derivado

'''

class pokemon:
    pass
    def __init__(self,name, type):
        self.name = name
        self.type = type
    
    def description(self):
        return '{} de tipo {}'.format(self.name,self.type)
    

class zubat(pokemon):
    def atack(self, atackType):
        return f"mi tipo de ataque es {self.atackType}"
    
class charmelion(pokemon):
    def atack(self, atackType):
        return 'mi nombre es {} con tipo de ataque {}'.format(self.name,atackType)
    
NewPokemon = zubat('joan','flight')
print(NewPokemon.description())
print(NewPokemon.atack('volador'))