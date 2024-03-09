alumnos = {}
cantidad = int(input("Ingresa cuantos alumnos: "))
for num in range(cantidad):
    alumno = (input("Nombre del alumno: "))
    while alumno in alumnos:
        print("Ya existe este alumno ")
        alumno = (input("Nombre del alumno: "))
    notas = []
    nota = int(input("Dame una nota del alumno (Negativo para terminar): "))
    while nota > 0:
        notas.append(nota)
        nota = int(input("Dame una nota del alumno (Negativo para terminar): "))
    alumnos[alumno] = notas.copy()

for alumno, notas in alumnos.items():
    print("%s ha sacado %f" % (alumno,sum(notas)/len(notas)))