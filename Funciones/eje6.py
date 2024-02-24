#crea una lasagna
"""Lista de ingredientes
pasta de lasagna
carne molida
tomate
cebolla
ajo
queso mozzarella
queso parmesano
sal
pimienta
"""
ingredientes = ["pasta de lasagna","carne molida","tomate","cebolla","ajo","queso mozzarella","queso parmesano","sal","pimienta"]

#Funcion para verificar los ingredientes
def verificarIngredient(ingredientes):
    for ingrediente in ingredientes:
        print(f"Verificando ingredientes: {ingrediente}")
        print("Todos las ingredientes estan listos.\n")
#Funcion para preparar la salsa 
def preparar_salsa():
    print("Preparando la salsa...\n")
    print("La salsa esta lista")

#Funcion para preparar la carne 
def preparar_carne():
    print("Preparando la scarne...\n")
    print("La carne esta lista")

#Funcion para hornear la lasagna
def hornear_lasagna():
    print("Hornear lasagna...\n")
    print("La lasagna esta lista")

#Funcion principal para preparar la lasagna
def preparar(ingrediente):
    verificarIngredient(ingrediente)
    preparar_salsa()
    preparar_carne()
    hornear_lasagna()

preparar(ingredientes)


