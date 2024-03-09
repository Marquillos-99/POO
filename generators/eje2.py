lista =[2,4,6,8,10]

cuadrado = [x**2 for x in lista]
print (cuadrado)

cuadradoG = (x**2 for x in lista)
for i in cuadradoG:
    print (i)