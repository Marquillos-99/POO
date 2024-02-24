def suma_lista(lista):
    if not lista:
        return 0
    else:
        return lista[0] + suma_lista(lista[1:])

lista = [1, 2, 3, 4, 5]
resultado = suma_lista(lista)
print(resultado)  # Salida: 15


def suma_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

lista = [1, 2, 3, 4, 5]
resultado = suma_lista(lista)
print(resultado)  # Salida: 15
