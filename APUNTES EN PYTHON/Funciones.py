#Se usan para simplificar y reusar codigo
#Sintaxis --> def nombre_funcion (parametros opcionales):
                #accion

from __future__ import division
from ast import arg


def nombre_funcion(nombre):
    print("Me llamo", nombre)
    
def operaciones_matematicas(a,b):
    def suma(a,b):
        return a+b
    
    def resta(a,b):
        return a-b
    
    def multiplicacion(a,b):
        return a*b
    
    def division(a,b):
        return a/b
        
    print ("El resultado de la suma es", suma(a,b))
    print ("El resultado de la resta es", resta(a,b))
    print ("El resultado de la multiplicacion es", multiplicacion(a,b))
    print ("El resultado de la division es", division(a,b))

def operaciones_tupla(a,b):
    return a+b, a-b, a*b, a/b

resultado = operaciones_tupla(23, 6)
print(resultado[3])
suma, resta, multi, divi = operaciones_tupla(23, 6)
print(suma)
print(resta)
print(multi)
print(divi)

def tiempo(frase):
    temperatura = 7.9
    print(frase, "una temperatura de", temperatura, "grados celsius")
    
def Mi_Nombre(nombre = "Javi"):
    print("Mi nombre es ", nombre)
    
def parametros_variables(*args):
    print(args)
    resultado = 0
    for iterado in args: 
        resultado += iterado
    print(resultado)

def diccionario(**kwargs):
    print(kwargs)
    if kwargs['Sevillafc']=="Grande de Andalucia":
        print("Se folla al Betis")

def sumador(**kwargs):
    elemento1 = kwargs['elemento1']
    elemento2 = kwargs['elemento2']
    resultado = 0
    for iterador in range(elemento1, elemento2 + 1):
        resultado +=iterador
    return resultado
print(sumador(elemento1 = 3, elemento2 = 3))

#funcion anonima: se tienen que asignar una variable que sea igual a una funcion. Sin def y sin return
sumatoria = lambda x:x+x

#Hay de invocarlas despues de ser definidas y meter su parametro  
print(sumatoria(2))
nombre_funcion("Javier Puente Piazza")
operaciones_matematicas(8,9)
tiempo("Hoy hace")
Mi_Nombre() 
parametros_variables(1,2,5,7,3,6,7,3,5)
diccionario(Sevillafc = "Grande de Andalucia", Betis = "Segundo equipo de la ciudad")
