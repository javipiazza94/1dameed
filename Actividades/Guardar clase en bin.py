from pickle import *
class vehiculo:
    nombre = ""
    precio = 0.0
    
    def __init__(self, nombre_j1, precio_j1):
        self.nombre = nombre_j1
        self.precio = precio_j1
        
    def __str__(self): 
        return f'Mi nombre es {self.nombre} y mi precio es {self.precio}'
    
    def getnombre (self):
        return self.nombre
    
j1 = vehiculo("Renault", 35000)
print(type(j1))
print(j1)


f = open('archivo binario.bin', 'w+b') 

dump(vehiculo, f)

f.seek(0)
nuevo_renault = load(f)

print(nuevo_renault)
f.close()