def introducirNumeros():
    global numero1, numero2
    numero1 = int(input("Introduzca el primer numero: "))
    numero2 = int(input("Introduzca el segundo numero: "))

def sumas(numero1,numero2):
    print(f"La suma de {numero1} + {numero2} = {numero1 + numero2}")

def resta(numero1,numero2):
    print(f"La resta de {numero1} - {numero2} = {numero1 - numero2}")

def multiplicacion(numero1,numero2):
    print(f"La multiplicacion de {numero1} * {numero2} = {numero1 * numero2}")

def division(numero1,numero2):
    print(f"La division de {numero1} / {numero2} = {numero1 / numero2}")

def potencia(numero1,numero2):
    print(f"La potencia de {numero1} ^ {numero2} = {numero1 ** numero2}")

def raizCuadrada(numero1):
    print(f"La raiz cuadrada de {numero1} = {numero1 ** 0.5}")

def modulo(numero1,numero2):
    print(f"El modulo de {numero1} % {numero2} = {numero1 % numero2}")

while True:
    print("""
    Ingrese una opcion:
    1. Suma
    2. Resta
    3. Multiplicacion
    4. Division
    5. Potencia
    6. Raiz Cuadrada
    7. Modulo
    8. Salir
""")
    
    election = int(input())

    if election == 1:
        introducirNumeros()
        sumas(numero1,numero2)
    elif election == 2:
        introducirNumeros()
        resta(numero1,numero2)
    elif election == 3:
        introducirNumeros()
        multiplicacion(numero1,numero2)
    elif election == 4:
        introducirNumeros()
        division(numero1,numero2)
    elif election == 5:
        introducirNumeros()
        potencia(numero1,numero2)
    elif election == 6:
        introducirNumeros()
        raizCuadrada(numero1,numero2)
    elif election == 7:
        introducirNumeros()
        modulo(numero1,numero2)
    elif election == 8:
        print("Adios")
        break
    else:
        print("Ingrese una opcion valida")