#creando constructor
#modificar un atributo

class Email:
    def __init__(self):
        self.enviado = False
        

    def enviarCorreo(self):
        self.enviado = True

mi_correo = Email()
print(mi_correo.enviado)

#para True primero llamas al objeto
mi_correo.enviarCorreo()
print(mi_correo.enviado)
