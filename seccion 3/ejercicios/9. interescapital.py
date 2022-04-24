"""Calcule el interés compuesto generado por un capital depositado 
durante cierta cantidad de tiempo a una tasa de interés determinada, 
aplique las siguientes formulas.
"""

from datetime import date

from sqlalchemy import VARCHAR


capital = float(input("ingrese la capital: "))
interes = float(input("ingrese la tasa de interes "))
tiempo = float(input("ingrese el tiempo necesario"))

monto = ((1+interes/100)** tiempo)*capital
tasainteres = monto - capital

print(str("el interes compuesto es: "), +float(interes))
print(str("el monto es: "), +float(monto))