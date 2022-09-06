#Instruccion
f = open('/Users/javip/OneDrive/Documents/DAM/ACTIVIDADES/EJERCICIOS DE PROGRAMACIÓN/PYTHON/APUNTES EN PYTHON/Fichero_a_leer.txt', 'r+') #Hay que escribir la ruta completa con los directorios separados en '/'
datos = f.readlines() #Aplicamos la funcion read() o readlines y lo guardamos en una variable para ser impresa. Podemos poner el numero de bytes a leer por parametro
print(datos)
f.close() #Cerramos

#PERMISOS
# r = lectura
# a = adjuntar, anadir al final del mismo
# w = escritura, se modifica entero
# x = crear automatico uno nuevo

#MODO
# t = texto
# b = binario
# + = implicito



