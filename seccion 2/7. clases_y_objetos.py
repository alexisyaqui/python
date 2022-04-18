#clases y objetos

class Pokemon():

    animal = "Pikachu"
     
#en el def init le pasamos los parametros de la clase e inicializamos las variables

    def __init__(self, poder, color, edad):
        self.poder = poder
        self.color = color
        self.edad = edad
    
    def saludar(self):
        print ("pika pika pika........")

    def mostrar_edad(self):

        print(f"la edad es: {self.edad}")

    def nueva_edad(self):
        if self.edad <= 60:
            self.edad += 2

            print(f"la nueva edad es: {self.edad}")
    
    def color_pokemon(self):
        print (f"el color del pokemon es: {self.color}")

    def poder_pokemon(self):
        print(f"el poder del pokemon es: {self.poder}")
    
    def edad_pokemon(self):
        print(f"la edad del pokemon es: {self.edad}")

    

#cerramos la clase y creamos el objeto
pokemon_1 = Pokemon("Electromagnetismo", "amarillo", 50)
pokemon_1.saludar()
pokemon_1.color_pokemon()
pokemon_1.poder_pokemon()
pokemon_1.edad_pokemon()
pokemon_1.nueva_edad()

print("\n")

pokemon_2 = Pokemon("rayo", "rojo", 43)
pokemon_2.saludar()
pokemon_2.color_pokemon()
pokemon_2.poder_pokemon()
pokemon_2.edad_pokemon()
pokemon_2.nueva_edad()

