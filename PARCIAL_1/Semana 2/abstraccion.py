from abc import ABC, abstractmethod

class Figura(ABC):  # Clase abstracta
    @abstractmethod
    def calcular_area(self):
        pass

class Cuadrado(Figura): #Creamos la clase
    def __init__(self, lado): #llamamos al cosntructor
        self.lado = lado

    def calcular_area(self):  #Creamos un metodo calcular
        return self.lado * self.lado #Retornamos el valor

mi_cuadrado = Cuadrado(4)  #Instanciamos la clase
print(mi_cuadrado.calcular_area())  #Imprimimos