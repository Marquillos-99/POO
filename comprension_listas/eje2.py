lista = []
for numero in range(0,11):
    lista.append(numero**2)

pares = []
for numero in lista:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)