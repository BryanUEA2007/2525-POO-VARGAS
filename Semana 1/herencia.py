class Animal:
    def hacer_sonido(self):
        return "Sonido genérico"

class Perro(Animal):  # Hereda de Animal
    def hacer_sonido(self):
        return "Guau guau"

mi_perro = Perro()
print(mi_perro.hacer_sonido()) #Imprimimos