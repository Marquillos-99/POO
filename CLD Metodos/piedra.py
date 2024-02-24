import random

opciones = ["piedra", "papel","tijeras"]

def eleccion():
    election = str(input("Elige una opcion  (Piedra, Papel, Tijeras):").lower())
    while election not in opciones:
        election = str(input("Elige una opcion  (Piedra, Papel, Tijeras):").lower())
    return election

def compu_seleccion():
    return random.choice(opciones)

def determinar(jugador, computadora):
    if jugador == computadora:
        return "Empate"
    elif jugador == "piedra" and computadora == "papel":
        return "Perdisto"
    elif jugador == "piedra" and computadora == "tijeras":
        return "Ganaste"
    elif jugador == "papel" and computadora == "piedra":
        return "Ganaste"
    elif jugador == "papel" and computadora == "tijeras":
        return "Perdiste"
    elif jugador == "tijeras" and computadora == "piedra":
        return "Perdiste"
    elif jugador == "tijeras" and computadora == "papel":
        return "Ganaste"
    
def main():
    jugador = eleccion()
    computadora = compu_seleccion()
    resultado = determinar(jugador, computadora)
    print(f"Jugador: {jugador}\nComputadora: {computadora}\nResultado: {resultado}")

if __name__ == "__main__":
    main()
