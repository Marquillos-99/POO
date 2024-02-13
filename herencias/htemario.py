class instrumento:
    def __init__(self, precio):
        self.precio = precio
        def tocar(self):
            print("estamos tocando ")

class Guitar(instrumento):
    def __init__(self, precio):
        super().__init__(precio)