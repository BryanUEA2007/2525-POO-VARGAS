# Creamos nuestra clase principal
class Animal:
    def __init__(self, nombre):  #Creamos nstro constructor
        self.__nombre = nombre  # Encapsulamos el atributo nombre

    def hacer_sonido(self):  #Creamos un metodo para hacer sonido
        return "El animal hace un sonido."

    def obtener_nombre(self):
        return self.__nombre  # Creamos el metodo para acceder al atributo privado



# Creamos nuestra clase hija que va a heredar de la clase padre animal
class Perro(Animal):
    def hacer_sonido(self):  #Creamos el metodo hacer sonido el cual va hacer una accion diferente
        return "¡Guau!" #  #Sobreescribimos el metodo de la clase padre


# Creamos otra clase llamada gato que de igual hereda de nuestra clase padre animal
class Gato(Animal):
    def hacer_sonido(self): #creamos el mismo metodo pero cn diferente accion
        return "¡Miau!"  # Volvemos a sobrrescribir el metodo


# Instanciamos los objetos con las clases
perro = Perro("Rex")
gato = Gato("Miau")

# Usamos el polimorfismo
animales = [perro, gato]
for animal in animales:
    print(f"{animal.obtener_nombre()} dice: {animal.hacer_sonido()}")
