#funciones 

from pprint import pprint


def suma(a = int , b= int):
    int = resultado = a + b
    return resultado

resultado = suma(2, 4)
print(int(resultado))


def MostrarEdad(message = " ", edad = 12):
    resultado_edad = message + str(edad)

    return resultado_edad

resultado_edad = MostrarEdad("la edad es: ")
print (resultado_edad)