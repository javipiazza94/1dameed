numero = 1492
"""
print(type(numero)) # Averiguamos el tipo (que no deja de ser una clase predefinida)
numero_a_texto = str(numero) #cambiamos el tipo a cadena y le asignamos nueva variable
print(type(numero_a_texto)) #imprimimos el tipo
print(numero_a_texto) #imprimimos la variable
print(repr(numero_a_texto))#Imprimimos la representacion para el desarrollo
"""

class juguete:
    nombre = ""
    precio = 0.0
    
    def __init__(self, nombre_j1, precio_j1):
        self.nombre = nombre_j1
        self.precio = precio_j1

#Se pueden sobrecargar metodos para que se vean bonitos con el .__str__
    def __str__(self): 
        return f'Mi nombre es {self.nombre} y mi precio es {self.precio}'
        
Lego = juguete("Lego McLaren f1", 199.98)
print(Lego) #Imprime el str por debajo
demo = Lego
print(type(demo)) #Imprime su clase
print(demo)
#print(repr(Lego))# Lo imprime para desarrolladores (representacion interna para maquina, tecnicas, depuracion, desarrollo)
#print(str(Lego))#Lo imprime para el usuario (representacion para humanos, usuarios)
