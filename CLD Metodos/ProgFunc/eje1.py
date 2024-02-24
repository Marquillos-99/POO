# def filtrar_pares(lista):
#     pares = []
#     for numero in lista:
#         if numero % 2 == 0:
#             pares.append(numero)
#     return pares

# lista = [1, 2, 3, 4, 5 ]
# numeros_pares = filtrar_pares(lista)
# print(numeros_pares)

def filtrar_pares(lista):
    return [numero for numero in lista if numero % 2 == 0]
 
lista = [1, 2, 3, 4, 5 ]
numeros_pares = filtrar_pares(lista)
print(numeros_pares)