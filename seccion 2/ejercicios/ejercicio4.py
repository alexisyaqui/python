print ("ingrese de datos del alumno")

curso = ["matematica", "ingles"]
nota = []

for ingresodatos in curso:
    nombreAlumno = input("ingrese el nombre del alumno: \t")
    nota1 = input("ingrese la nota del alumno \t")
    nota.append(nota1)

for ingresonota in range(len(nota)):
    print ("ela nota del curso alumno \t" curso[ingresonota] + "la nota es \t" + nota[ingresonota])