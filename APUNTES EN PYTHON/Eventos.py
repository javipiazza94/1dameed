import tkinter
from tkinter import ttk
ventana = tkinter.Tk()

#EVENTOS
def saludar (event):
    print("Heil Hitler")
def saludarDoble (event):
    print("Hitler tenia razon")
def salir(event):
    print("Nos vemos")
    ventana.quit()
    
boton = tkinter.Button(ventana, text="Dale al boton")
boton.pack()
boton.bind('<Button-1>', saludar)
boton.bind('<Double-1>', saludarDoble)

botonSalir = tkinter.Button(ventana, text="Salir")
botonSalir.pack()
botonSalir.bind('<Button-1>', salir)
ventana.mainloop() 