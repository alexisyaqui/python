"""
Enunciado: Crear un programa para encontrar el Área de un Círculo, use la formula.

Área (A): Es el área del círculo.

PI (?): Representa el valor constante pi (3.14159)

Radio (r): Es el radio del círculo.

Análisis: Para la solución de este problema, se requiere que el usuario ingrese el radio del círculo y el sistema procesa y obtiene el Área del círculo. Expresión Matemática

Expresión Algorítmica

A <== 3.14159 * r * 2

Entrada

· Radio (r).

Salida

· Área (a).

Preguntas de esta tarea
Se requiere que el usuario ingrese el radio del círculo y el sistema procesa y 
obtiene el Área del círculo.
"""

pi = 3.14159

area = float(input("ingrese el area del circulo"))
radio = float(input("ingrese el radio del circulo"))

areacirculo = (pi * radio * 2)

print(f"el area del circulo es: ", +float(areacirculo))