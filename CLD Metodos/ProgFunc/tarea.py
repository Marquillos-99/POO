from random import randint

def tirar_dados():
    dado1 = randint(1,6)
    dado2 = randint(1,6)
    return dado1, dado2

def jugar_dados():
    tirada1,tirada2 = tirar_dados()
    suma = tirada1 + tirada2
    print(f"Tirada 1: {tirada1}")
    print(f"Tirada 2: {tirada2}")
    print(f"Suma: {suma}")

def main():
    for i in range(10):
        jugar_dados()

if __name__ == "__main__":
    main()