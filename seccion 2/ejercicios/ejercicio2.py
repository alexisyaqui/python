
#Escribir un programa que almacene las asignaturas de un curso 
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista,
# pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por 
# pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las 
# asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.


from turtle import clear


curso = ["Matematicas", "Fisca", "Quimica", "Historia", "Lengua"]
nota = []

for cursos in curso:
    nota1 = input("ingrese la nota del estudiante")
    nota.append(nota1)

for i in range(len(curso)):
    print("en nota " + nota[i] + " ha has sacado " + curso[i])
    
