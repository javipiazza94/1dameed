
import tkinter
from tkinter import ttk
ventana = tkinter.Tk()

frame = ttk.Frame(ventana) #Es una subventana que agrupa cosas
frame.grid(column = 0, row = 0, sticky= tkinter.N)

#ETIQUETAS
Etiqueta = tkinter.Label(frame, text="Hola")
Etiqueta.grid(column = 0, row = 0, sticky= tkinter.N, padx = 10, pady = 10)

#LISTAS
#lista = ['Augusto', 'Cesar', 'Juliano el Apostata', 'Constantino', 'Teodosio', 'Honorio', 'Trajano']
#lista_items = tkinter.StringVar(value=lista)
#Listbox = tkinter.Listbox(ventana, height = 50, listvariable=lista_items)
#Listbox.grid(column = 0, row = 0, sticky= tkinter.S)

#RADIOBUTTONS
Seleccionado = tkinter.StringVar()
r1 = ttk.Radiobutton(frame, text="Si", value = 1, variable=Seleccionado)
r2 = ttk.Radiobutton(frame, text="No", value = 2, variable=Seleccionado)
r3 = ttk.Radiobutton(frame, text="Tal vez", value = 3, variable=Seleccionado)

r1.grid(column = 2, row = 1, sticky= tkinter.N, padx = 10, pady = 10)
r2.grid(column = 2, row = 2, sticky= tkinter.N, padx = 10, pady = 10)
r3.grid(column = 2, row = 3, sticky= tkinter.N, padx = 10, pady = 10)

#CHECKS
def Mifuncion():
    print("Viva Espana, Viva el Rey, Viva el Orden y la Ley")
    
check = ttk.Checkbutton(ventana, text='Check', variable= Seleccionado, command=Mifuncion)
check.grid(column=3, row=0, sticky=tkinter.W, pady=15, padx=15)


ventana.mainloop() 