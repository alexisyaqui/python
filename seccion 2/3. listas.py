lista_objetos = [1,2,3,"nombres",[10,20,30,[1,2,3,]], True]
lista = []#listas vacias
lista = list() #variable reservada list

#accediendo a los elementos de una lista

print (lista_objetos[3])
print (lista_objetos[4][3][2])

#agregar listas al objeto

print("ESTE ES EL LISTADO INICIAL", lista_objetos)
print(lista_objetos.append("PYTHON ES GENIAL"))
print( lista_objetos)

#eliminar un objeto de una lista)
print(lista_objetos.pop(3))#POP SIRVE PARA ELIMINAR UN OBJETO EN UNA LISTA
print(lista_objetos)

#ORDENAR LAS LISTAS CON LA FUNCION SORTED
print()
print("ORDEN DE NUMERO CON LA FUNCION SORTED")
orden_numero = [43,-2, -1, 100, 0, 12, 1, 2, 1, 10, 2333]
orden_numero = sorted(orden_numero)
print(orden_numero)



#recorrer listas 

lista_usuario = ["juan", "manuel", "luis", "melvin"]
tamaño_usuario = len(lista_usuario)


print ("RECORRIENDO LISTAS")


for usuario in lista_usuario:
    if usuario == "juan":
        print("el usuario no tiene multas")
    elif usuario == "manuel":
        print ("este usuario tiene multa")
    elif usuario == "luis":
        print ("este usuario se se encuentra solvente")
    elif usuario == "melvin":
        print("este usuario tiene orden de apresion")


print ("recorremos las listas")

for recorrer_lista in range(tamaño_usuario):
    print ((lista_usuario[recorrer_lista]))