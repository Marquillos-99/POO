import math 

def calcular_area(tipo_figura, dimensiones):
  """
  Calcula el área de una figura geométrica usando casos.

  Args:
    tipo_figura: El tipo de figura geométrica (triángulo, cuadrado, rectángulo, círculo).
    dimensiones: Una lista con las dimensiones de la figura.

  Returns:
    El área de la figura geométrica.
  """
  match tipo_figura:
    case "triangulo":
      base, altura = dimensiones
      area = (base * altura) / 2
    case "cuadrado":
      lado = dimensiones[0]
      area = lado ** 2
    case "rectangulo":
      base, altura = dimensiones
      area = base * altura
    case "circulo":
      radio = dimensiones[0]
      area = math.pi * radio ** 2
    case _:
      raise ValueError("Tipo de figura no válida")

  return area

def main():
  """
  Función principal del programa.
  """
  # Pedir al usuario el tipo de figura
  tipo_figura = input("Introduzca el tipo de figura (triángulo, cuadrado, rectángulo, círculo): ").lower()

  # Pedir al usuario las dimensiones de la figura
  dimensiones = []
  for i in range(1, 3):
    dimension = float(input(f"Introduzca la dimensión {i}: "))
    dimensiones.append(dimension)

  # Calcular el área de la figura
  area = calcular_area(tipo_figura, dimensiones)

  # Mostrar el resultado al usuario
  print(f"El área de la {tipo_figura} es de {area}")

if __name__ == "__main__":
  main()
