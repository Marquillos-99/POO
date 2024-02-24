# def ordenar(lista):
#     for i in range(len(lista)):
#         for j in range(len(lista)-1):
#             if lista[j] > lista[j+1]:
#                 lista[j], lista[j+1] = lista[j+1], lista[j]
#     return lista

# lista_numeros = [5,3,4,1,2]
# numerosBien = ordenar(lista_numeros)
# print (numerosBien)
def ordenar_por_insercion(lista):
    def insertar(elemento, lista_ordenada):
        if not lista_ordenada:
            return [elemento]
        elif elemento <= lista_ordenada[0]:
            return [elemento] + lista_ordenada
        else:
            return [lista_ordenada[0]] + insertar(elemento, lista_ordenada[1:])

    return lista if len(lista) <= 1 else insertar(lista[0], ordenar_por_insercion(lista[1:]))

lista_numeros = [5, 2, 4, 1, 3]
numeros_ordenados = ordenar_por_insercion(lista_numeros)
print(numeros_ordenados)  

        