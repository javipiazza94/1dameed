import tkinter #importamos libreria
from tkinter import ttk

ventana = tkinter.Tk() #inicializamos objeto ventana
def Accion(event):
    print(("Comeme los cojones"))
def Salir(event):
    print(("Chupamela perro"))
    ventana.quit()
#Geometría Grid/rejilla --> estilo hojas del Excel. columnconfigure(numeracion columna, weight=nºfilas)
#(0,0) (1,0)
#(0,1) (1,1)
#(0,2) (1,2)

#(usuario) (entrada)
#(contraseña) (entrada)
#              (boton)

#Confguranos el grid
ventana.columnconfigure(0, weight=3)
ventana.columnconfigure(1, weight=5)

#etiquetas y entradas
usuario = ttk.Label(ventana, text="Introduce tu nombre de usuario")
usuario.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5) #Lo introducimos en el grid. Sticky = posicion de brujula
usuario_entrada = ttk.Entry() #Creamos la entrada de usuario
usuario_entrada.grid(column=1, row=0, sticky=tkinter.W, padx=5, pady=5)

contraseña = ttk.Label(ventana, text="Introduce tu nombre de contraseña")
contraseña.grid(column=0, row=1, sticky=tkinter.W, padx=5, pady=5) #Lo introducimos en el grid. Sticky = posicion de brujula
contraseña_entrada = ttk.Entry(show="*") #Creamos la entrada de usuario
contraseña_entrada.grid(column=1, row=1, sticky=tkinter.W, padx=5, pady=5)

#botones
boton_entrada = ttk.Button(ventana, text="ACCEDE" )
boton_entrada.grid(column=1, row=2, sticky=tkinter.W, padx=5, pady=5)
boton_salida = ttk.Button(ventana, text="SALIR" )
boton_salida.grid(column=0, row=2, sticky=tkinter.W, padx=5, pady=5)
boton_entrada.bind('<Double-1>', Accion)
boton_salida.bind('<Button-1>', Salir)

Seleccionar_botones = tkinter.StringVar()
B1 = ttk.Radiobutton(ventana, text="verdadero", value='1', variable=Seleccionar_botones)
B2 = ttk.Radiobutton(ventana, text="falso", value='2', variable=Seleccionar_botones)
B3= ttk.Checkbutton(ventana, text="Acepto las condiciones del servicio", variable=Seleccionar_botones)
B1.grid(column=1, row=3, padx=5, pady=5)
B2.grid(column=1, row=4, pady=5, padx=5)
B3.grid(column=1, row=5, pady=5, padx=5)

#Listas
lista = ["Goering", "Goebbels", "Eichmann", "Mengele"]
lista_items = tkinter.StringVar(value=lista)
listbox = tkinter.Listbox(ventana, height=10, listvariable=lista_items)
listbox.grid(column=0, row=3, sticky=tkinter.W)

ventana.mainloop() #generamos ventana mendiante un bucle



