class Animals:
    def __init__(self,name):
        self.name = name 
        def animal_type(self):
            pass

class Lion(Animals):
    def animal_type(self):
        print('Animal salvajes')

class Dog(Animals):
    def animal_type(self):
        print('animal domestico')

new_animal1 = Lion("Mufasa")
new_animal1.animal_type()

new_animal2 = Dog('Roca')
new_animal2.animal_type()