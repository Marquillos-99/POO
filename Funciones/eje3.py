"""
Función de máximo común divisor (MCD): Escribe una función que tome dos números como argumentos y devuelva su máximo común divisor.
"""
def mcd(num1,num2):
    while num2:
        num1,num2 = num2, num1 % num2
        return num1
    
num1 = 144
num2 = 12
mcd_result = mcd(num1,num2)
print(f"El MCD de {num1} y {num2} es: {mcd_result}")