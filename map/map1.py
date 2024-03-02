#sintaxis map(function,objeto iterable)
def cuadrado (numero):
    return numero * numero 

lista = [1,2,3,4,5]
resultado = map(cuadrado,lista)

lista_final = list(resultado)

print(lista_final)