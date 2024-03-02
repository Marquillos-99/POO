multiplicar_por = lambda n: lambda x : x *n

multiplicar_dos = multiplicar_por(2)
multiplicar_tres = multiplicar_por(3)
multiplicar_diez = multiplicar_por(10)

resultado_dos = multiplicar_dos(5)
resultado_tres = multiplicar_tres(5)
resultado_diez = multiplicar_diez(5)

print(f"Resultado dos: {resultado_dos}")
print(f"Resultado tres: {resultado_tres}")
print(f"Resultado diez: {resultado_diez}")