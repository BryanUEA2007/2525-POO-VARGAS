class Gato:  #Definimos la clase
    def hacer_sonido(self): #Llamamos al metodo
        return "Miau miau"

class Pajaro:  #Definimoss la clase
    def hacer_sonido(self):
        return "Pío pío" #Retornamos el sonido

def reproducir_sonido(animal):  #Creamos una funcion
    print(animal.hacer_sonido())

reproducir_sonido(Gato())  # Llamos a la funcion e imprimimos
reproducir_sonido(Pajaro())