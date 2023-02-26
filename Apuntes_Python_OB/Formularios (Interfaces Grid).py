# Una interfaz grafica es una implementacion visual de un codigo que permite interactuar el hombre con el programa
# Antiguamente era solo de texto, y ahora hay mucha mas visualidad
# Opciones: PyGTK o PyQT o wxPython o Tkinter

#tkinter viene de serie. Viene del lenguaje TCL que es reinterpretado

import tkinter
from tkinter import ttk #Importamos estilo

#Contienen widgets o componentes contenidos en ventanas y cuadros --> etiquetas,   controles, botones, comprobadores, etc

#Iniciamos la ventana
ventana = tkinter.Tk()

#Creamos los componentes. #Los colocamos mediante las geometrias, que posicionan los objetos en un determinado orden. #Estamos usando la geometria pack, coloca los elementos de izquierda a derecha y de arriba a abajo

#Gemetria Grid (matrices, como una hoja de calculo)
#(0,0) (1,0) (2,0) (3,0)
#(0,1) (1,1) (2,1) (3,1)
#(0,2) (1,2) (2,2) (3,2)
#(0,3) (1,3) (2,3) (3,3)

ventana.columnconfigure(0, weight=1) #Le decimos que queremos 1 columna con 1 elemento
ventana.columnconfigure(1, weight=3) #Le decimos que queremos 1 columna con 3 elementos

# (0.0) (1.0) (2.0)
# (0.1) (1.1) (2.1)

#Hacemos usuario y contrasena con etiquetas y entradas
Usuario = ttk.Label(ventana, text = "Usuario")
Usuario.grid(column = 0, row = 0, sticky= tkinter.N, padx = 10, pady = 10) #Posicion "Rosa de los vientos"
Usuario_entrada = ttk.Entry(ventana) # Entrada de texto
Usuario_entrada.grid(column = 1, row = 0, sticky = tkinter.S, padx = 10, pady = 10)

Contrasena = ttk.Label(ventana, text = "Contrasena")
Contrasena.grid(column = 0, row = 1, sticky= tkinter.N, padx = 10, pady = 10) #Posicion "Rosa de los vientos"
Contrasena_entrada = ttk.Entry(ventana, show = "*") # Entrada de texto
Contrasena_entrada.grid(column = 1, row = 1, sticky = tkinter.S, padx = 10, pady = 10)

#Botones
Acceso_boton = ttk.Button(ventana, text = "Accede")
Acceso_boton.grid(column=1, row = 2, sticky=tkinter.S, padx=20, pady= 10)

#Crea un bucle para que pueda verse hasta que decida cerrarlo
ventana.mainloop() 

