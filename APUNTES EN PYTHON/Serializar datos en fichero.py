#Se pueden guardar los estados de los programas sin guardarlos en bases de datos
import pickle
class juguete:
    nombre = ""
    precio = 0.0
    
    def __init__(self, nombre_j1, precio_j1):
        self.nombre = nombre_j1
        self.precio = precio_j1
        
    def __str__(self): 
        return f'Mi nombre es {self.nombre} y mi precio es {self.precio}'
    
    def getnombre (self):
        return self.nombre
    
j1 = juguete("PS5", 350)
print(type(j1))
print(j1)

#f = open('archivo binario.bin', 'wb') #Lo hemos serializado y guardado en un archivo .bin
#pickle.dump(j1, f)
#f.close()

f = open('archivo binario.bin', 'rb') #Puedo deserializarlo desde el archivo e imprimirlo de nuevo
ps5 = pickle.load(f)
f.close

print(ps5.getnombre(), ps5.precio)