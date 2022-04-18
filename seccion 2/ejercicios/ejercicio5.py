import sys
dato = sys.stdin.readlines()
dato_nuevo = [cadena.replace("\n", "")for cadena in dato]
rango = int(dato_nuevo[0])
dato_nuevo.pop(0)
busqueda_dato = dato_nuevo[rango:]
valores = dato_nuevo[:rango]
valores_nuevos = [cadena.replace(" ", "=") for cadena in valores]

string_inicial = ",".join(valores_nuevos)
diccionario_final = dict(item.split("=") for item in
string_inicial.split(","))
for elemento in busqueda_dato:
    if elemento in diccionario_final:
        print (elemento + "=" + diccionario_final[elemento])
    else:
        print ("Not found")