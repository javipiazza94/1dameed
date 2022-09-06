import Operaciones
import pprint
import math

def interruptor(estado):
    estado = True
    pprint.pprint(locals()) #Devuelve lo que contiene la funcion en su ambito local (no las globales)

interruptor(False)

Operacion_A = Operaciones.operaciones_matematicas(2,7)
#help(Operacion_A) #Devuelve la implementacion

Operacion_B = "Cayo Octavio Turino"
pprint.pprint(dir(Operacion_B)) #Mostramos en lista las propiedades del objeo Operacion_B

print("Propiedades del modulo MATH")
pprint.pprint(dir(math)) #Mostramos en lista las propiedades del modulo MATH

pprint.pprint(globals()) # Devuelve lo que contiene el programa en ejecucion en su ambito global (no muestran las de ambito local) --> Tabla de simbolos
