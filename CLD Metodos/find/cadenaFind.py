cadena = "El rápido zorro marrón salta sobre el perro perezoso."
subcadena = "zorro"

posicion = cadena.find(subcadena, 10, 25)

if posicion != -1:
  print(f"La subcadena '{subcadena}' se encuentra en la posición {posicion}")
else:
  print(f"La subcadena '{subcadena}' NO se encuentra en la cadena dentro del rango especificado.")