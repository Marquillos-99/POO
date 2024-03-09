#lista = []
#for numero in range(0,11):
#    lista.append(numero**2)

#pares = []
#for numero in lista:
#    if numero % 2 == 0:
#        pares.append(numero)

#print(pares)

lista = [numero for numero in [numero**2 for numero in range(0,11)] if numero % 2 == 0]
print(lista)