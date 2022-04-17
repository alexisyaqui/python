#tuplas, sets, o diccionarios

tupla_numeros = (1,2,4,5,6,7,34)
tupla_numeros_dos = tuple(["hola", "amigos", "ooooo"])
print(tupla_numeros)
print(tupla_numeros_dos)

fusion_tuplas = tupla_numeros + tupla_numeros_dos
print(fusion_tuplas)

#sets sirve para imprimir datos no repetidos.  eliminar los datos duplicados
conjunto_numeros = {1,2,3,2,2,2,3,4,5,5,5,5,65,3}
print(conjunto_numeros)


eliminacion_duplicado = ["hola", "hola", "como", "estas", "si", 1, 2, 3, 4, 5,]
eliminacion_duplicado = set(eliminacion_duplicado)
print (eliminacion_duplicado)

operacionuno = ["hola", "juan", "luis", "jorge"]
operaciondos = (1,2,3,3,4,5,65,7, 6)

operacion = conjunto_numeros.union(operacionuno)
#print (operacion)
print(operacion)


print()
#DICCIONARIOS 

persona = {
    'usuario':[10],
    'usuario2':[200],
    'usuario3': {
        'edad': [23],
        'fecha': [2]
    }
}
print(persona['usuario'])
print(persona['usuario2'])
print(persona['usuario3'])

#ejemplo

verduras = {

}

verduras ['caja1'] = ["papa", "limon", "guiskil"]
verduras ['caja2'] = ["papa", "limon", "guiskil"]

for key, values in verduras.items():
    if key == key:
        print(key, values)


