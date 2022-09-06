#Sirve para definir un conjunto de funciones comunes. Contienen parcialidades de una funcionalidad, dejando al programador la implementacion concreta
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sonido(self):
        pass
    def Hola(self):#No hace falta incocarlo en el resto de clases porque es generico y hereda a sus clases hijas
        print("Hola")
    
class perro(Animal):
    def sonido(self):#Hay que invocarlo especificamente
        print("Guau")
class gato(Animal): #Hay que invocarlo especificamente
    def sonido(self):
        print("Miau")
    
Pepe = perro()
Rodolfo = gato()
Pepe.sonido()
Rodolfo.sonido()
Rodolfo.Hola()

