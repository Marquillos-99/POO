from random import randint
#combinar funciones
# def tirar_dados(veces):
#   for i in range(veces):
#     dado1 = randint(1, 6)
#     dado2 = randint(1, 6)
#     suma = dado1 + dado2
#     print(f"Tirada {i + 1}: {dado1}")
#     print(f"Tirada {i + 1}: {dado2}")
#     print(f"Suma: {suma}")

# if __name__ == "__main__":
#   tirar_dados(10)

"""________________________________________________________________________________________________________________"""

#usar lista para almacenar los resultados
def tirar_dados(veces):
  resultados = [randint(1, 6) + randint(1, 6) for _ in range(veces)]

  for tirada, resultado in enumerate(resultados):
    print(f"Tirada {tirada + 1}: {resultado}")

if __name__ == "__main__":
  tirar_dados(10)

