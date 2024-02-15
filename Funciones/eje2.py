"""
Función de inversión de cadena: Escribe una función que tome una cadena como argumento y devuelva la cadena invertida.
start,stop,step
"""
"""
def invertir_cadena(cadena):
    cadena_invertida = ""
    for i in range(len(cadena)-1,-1,-1):
        cadena_invertida += cadena[i]
    return cadena_invertida

cadena = "Hola Mundo!"
cadena_invertida = invertir_cadena(cadena)
print(f"Cadena original: {cadena}")

print(f"Cadena invertida: {cadena_invertida}")

# for i in range(inicia, termina) (inicio,final, paso)

"""

def invertir_cadena(cadena):
    return "".join(reversed(cadena))

cadena = "Hola Mundo!"
cadena_invertida = invertir_cadena(cadena)
print(f"Cadena original: {cadena}")

print(f"Cadena invertida: {cadena_invertida}")