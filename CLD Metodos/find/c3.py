cadena = "Hola Mundo!"
subcadena = "mundo"

posicion = cadena.lower().find(subcadena.lower())

if posicion != -1:
  print(f"La subcadena '{subcadena}' se encuentra en la posición {posicion}")
else:
  print(f"La subcadena '{subcadena}' NO se encuentra en la cadena.")
