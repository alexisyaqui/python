
numero = int(input("ingrese el dato: \n"))

residuo = numero % 10
numero = numero // 10
inverso = residuo * 10

residuo = numero % 10
numero = numero // 10
inverso = (inverso + residuo) * 10

residuo = numero % 10
numero = numero // 10
inverso = (inverso + residuo) * 10

residuo = numero % 10
numero = numero // 10
inverso = (inverso + residuo) * 10


inverso = inverso + numero

print ('inverso', +numero)