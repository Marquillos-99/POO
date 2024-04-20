#def fibonacci(numero):
#    if numero == 0:
#        return 0
#    elif numero == 1:
#        return 1 
#    else:
#        return fibonacci(numero - 1) + fibonacci(numero - 2)
#    
#n = int(input("Introduzca un numero "))
#print(f"EL {n}` numero de la sucesion de fibonacci es {fibonacci(n)}")

def fibonacci(n):
    a,b = 0,1
    fibs = []
    for i in range(n):
        fibs.append(a)
        a, b = b, a+b
    return fibs

numero = int(input("Introduzca un numero "))
if numero <1:
    print("erros, no hay negativos en fibo")
else:
    fibs = fibonacci(numero)
    print(f"Los {numero} primeros numeros de fibo son {fibs}")