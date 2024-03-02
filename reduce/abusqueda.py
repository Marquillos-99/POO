lista2=['Mexico', 'Colombia', 'Brasil', 'Venezuela', 'Bolivia', 'Argentina', 'Uruguay', 'Peru', 'Paraguay', 'Chile','a']
a = list()
listafin = map(str.lower, lista2)
def contarconfor(lista):
    for x in lista:
        contar = 0
        for g in x:
            if g == 'a':
                contar = contar +1
        print(contar)
        a.append(contar)

contarconfor(listafin)
print("\nSum: ",sum(a))
