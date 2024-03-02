lista2=['Mexico', 'Colombia', 'Brasil', 'Venezuela', 'Bolivia', 'Argentina', 'Uruguay', 'Peru', 'Paraguay', 'Chile','a']

a = list(map(lambda x: x.lower().count("a"),lista2))

print(a)
print("\nSum:",sum(a))