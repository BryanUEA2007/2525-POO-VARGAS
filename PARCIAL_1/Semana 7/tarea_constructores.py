#Creamos una clase persona que almacene la edad y nombre
class Persona:
    def __init__(self, nombre, edad): #Inicializamos los atributos de nombre y  edad
        self.nombre = nombre
        self.edad = edad
        print(f"Persona creada: {self.nombre}, Edad: {self.edad}") #Imprimimos el nombre y la edad

    def presentar(self): #Creamos un metodo para preserntar a la persona
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")  #Imrprimimos la presentación

    def __del__(self):  #Creamos el constructor que muestra un mensaje al destruir la instancia
        print(f"Persona destruida: {self.nombre}")

# Creamos una instancia de la clase Persona
persona1 = Persona("Jose", 24)

# Llamos al metodo presentar y presentamos  a la persona
persona1.presentar()

# Eliminar la instancia para activar el destructor
del persona1