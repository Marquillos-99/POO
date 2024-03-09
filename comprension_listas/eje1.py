lista = []
#for numero in range(0,11):
#    if numero % 2 == 0:
#        lista.append(numero)
#print(lista)

lista = [numero for numero in range(0,11) if numero % 2 == 0]
print(lista)
