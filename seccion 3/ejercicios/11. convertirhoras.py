"""
Crear un programa que permita convertir una cantidad de 
segundos en horas, minutos y segundos.
"""

tiempo = float(input("ingrese el dato del tiempo \t"))

hora = 3600
minutos = 60


h = tiempo // hora
tiemposegundos = tiempo % hora
minutos = tiempo //minutos
tiemposegundos = tiempo % minutos

print(str("la hora es: "), + float(h))
print(str("los minutos es: "), + float(minutos))
print(str("la segundos es: "), + float(tiemposegundos))