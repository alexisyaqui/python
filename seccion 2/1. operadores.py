#operadores logicos and, or, not true 

edad = 112
operador_and = edad >= 18 and edad <30
operador_or = edad>= 18 or edad<=50
operdor_negacion = not True

print (operador_and)
print (operador_or)
print (operdor_negacion)


numero1 = 25
numero2 = -3.21
numero3 = 0
numero4 = 2

print(bool(numero1))
print(bool(numero2))
print(bool(numero3))
print(bool(numero4))


#condiciones if

numero = 34

if (numero >=18 ):
    print("el numero ingresado es mayor ")

    if (numero <=15):
        print("el numero ingresado es menor de edad")

    else:
        print("muchas gracias por su atencion")

elif(numero >=20):
    print("muchas gracias pero su hijo es enor edad")

else:
    print("gracias")