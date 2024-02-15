"""
Función de conteo de palabras: Escribe una función que tome una cadena (una frase o un párrafo) como argumento y devuelva un diccionario con el conteo de cada palabra en la cadena.
"""

def contar_palabras(cadena):
  """
  Cuenta la frecuencia de cada palabra en una cadena.

  Parámetros:
    cadena (str): La cadena a analizar.

  Retorno:
    dict: Un diccionario con las palabras como claves y su frecuencia como valores.
  """
  
def contar_palabras(cadena):
  """
  Cuenta la frecuencia de cada palabra en una cadena.

  Parámetros:
    cadena (str): La cadena a analizar.

  Retorno:
    dict: Un diccionario con las palabras como claves y su frecuencia como valores.
  """
def contar_palabras(cadena):
  """
  Cuenta la frecuencia de cada palabra en una cadena.

  Parámetros:
    cadena (str): La cadena a analizar.

  Retorno:
    dict: Un diccionario con las palabras como claves y su frecuencia como valores.
  """
  # Eliminar signos de puntuación
  cadena = re.sub(r'[^\w\s]|\n', ' ', cadena)

  # Convertir la cadena a minúsculas y dividirla en palabras
  palabras = cadena.lower().split()

  # Crear un diccionario para almacenar el conteo de palabras
  conteo_palabras = {}
  for palabra in palabras:
    # Ignorar palabras vacías
    if len(palabra) > 0:
      # Si la palabra ya está en el diccionario, aumentar su frecuencia
      if palabra in conteo_palabras:
        conteo_palabras[palabra] += 1
      # Si la palabra no está en el diccionario, agregarla con una frecuencia de 1
      else:
        conteo_palabras[palabra] = 1

  return conteo_palabras
