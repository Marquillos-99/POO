def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
numero = int(input("Ingrese un numero positivo "))
if numero < 0: 
    print("El numero no puede ser negativo")
else:
    resultado = factorial(numero)
    print(f"El factorial de {numero} es {resultado}")