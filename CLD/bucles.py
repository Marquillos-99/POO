#while
#edad = 0

#while edad < 18:
#    edad = edad + 1
#    print(f"Felicidades, tienes {edad}")

#secuencia = ["uno","dos","tres"]
#for elemento in secuencia:
#    print(elemento)

#edad = int(input("Cual es tu edad?"))
#if edad >= 18:
#    print(f"Felicidades, tienes {edad} puedes entrar a la discoteca")
#else:
#    print(f"Lo siento, no cumples con la edad para entrar a la discoteca")

estandar = 10.99
premium = 16.59
pro = 22.39


categoria = str((input("cual es tu categoria?")))

if (categoria == "estandar"):
    print(f"El precio final es de {estandar}")
elif (categoria == "premium"):
    print(f"El precio final es de {premium}")
else:
    print(f"El precio final es de {pro}")