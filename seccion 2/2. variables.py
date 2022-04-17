#variable de tipo strings

from turtle import clear


nombrepersona = ""

#variable de tipo intero


numeroUno = 2

#variables de tipo flotantes

numerodos = 3.23

#variable de tipo booleano

valor_booleano = True
valor_booleano_2 = False


listas = list()

diccionario = dict()

print (type(nombrepersona))
print (type(numeroUno))
print (type(numerodos))
print (type(valor_booleano))
print (type (valor_booleano_2))
print (type(listas))
print (type(diccionario))


#operadores aritmeticos

suma = 1+2
resta = 4-2
multiplicaion = 3*3
division = 10/2
potencia = 3**3
modulo = 20%3

print (suma)
print(resta)
print(multiplicaion)
print(division)
print(potencia)
print(modulo)


#convertir un numero a entero

numerotexto = "123"
numero = 3

resultado = int(numerotexto) + numero

print ("el resultado es: ", + resultado)


#ingreso de dato por medio de teclado

variabelnombre = input("ingrese un nombre ")
variable_edad = int(input("ingrese la edad del usuario: "))

mensaje = "el nombre del usuario es :" + str(variabelnombre) + "la edad del usuario es : " + str(variable_edad)

print (mensaje)
