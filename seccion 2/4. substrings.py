saludo = ("hola mundo este es un ejemplo para practicar python, porque me encanta python")

#la variable count sirve para hacer conteo de palabras dentro de una lista
conteo_letra = saludo.count("python")
print(conteo_letra)

#la variable find sierve para hacer conteo de espacio a partir de su posicion ya que un espacio es un dato string
conteo_expacio = saludo.find(" ")
print (conteo_expacio)

#slice para capturar un tamaño de un string

slice_word = saludo.find("me encanta python")
slice_word = saludo[slice_word : len(saludo)]
print (slice_word)

contexto = saludo.find(saludo)
contexto = saludo[contexto : len(saludo)]
print (contexto)

#conteo de espacios total
numeroletras = 0
for letra in saludo:
    if letra ==" ":
        numeroletras +=1

print("los numeros de espacios son: \t")
print(numeroletras)

cantidad_alumnos = 60000
despedida = f"adios en la proxima clase {cantidad_alumnos} en la escuela"
despedida.capitalize()
print(despedida)