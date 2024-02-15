"""
Función de ordenación de lista: Escribe una función que tome una lista de números como argumento y devuelva la lista ordenada de menor a mayor.
"""
def ordenar_lista(lista):
    lista_ordenada = sorted(lista)

    return lista_ordenada

numeros = ["Jose","Ana","Pedro","Maria"]
lista_ordenada = ordenar_lista(numeros)
print(f"Lista ordenada {lista_ordenada}")