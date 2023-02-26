import random
import tkinter
from tkinter import NW, ttk

ventana = tkinter.Tk()
colores = ['blue', 'yellow', 'red', 'green', 'purple']
for x in range(0,10):
    color = random.randint(0, len(colores) -1)
    color2 = random.randint(0, len(colores) -1)
    ancho = random.randint(0,50)
    alto = random.randint(0,50)
    etiqueta = tkinter.Label(ventana, text = "Collage", bg = colores[color], fg = colores[color2])
    etiqueta.place(x = random.randint(0,100), y = random.randint(0,100))
    
etiqueta = tkinter.Label(ventana, text = "Posicionamiento absoluto", bg = 'black', fg = 'white')
etiqueta.place(x = 45, y =68)
etiqueta2 = tkinter.Label(ventana, text = "Posicionamiento relativo", bg = 'brown', fg = 'orange')
etiqueta2.place(relx = 0.25, rely = 0.25, relwidth=0.5, anchor=NW)
ventana.mainloop() 
