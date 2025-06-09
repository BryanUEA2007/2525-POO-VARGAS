class Persona:  #Creamos la clase
    def __init__(self, nombre, edad):  #LLamamos a nuestro metodo constructor
        self.__nombre = nombre  # Atributo privado
        self.__edad = edad  # Atributo privado

    def obtener_info(self):  #Creamos un metodo
        return f"Nombre: {self.__nombre}, Edad: {self.__edad}"

mi_persona = Persona("Juan", 30) #Instanciamos la clase
print(mi_persona.obtener_info())  #Imprimimos