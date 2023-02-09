import tkinter #importamos libreria

ventana = tkinter.Tk() #inicializamos objeto ventana

etiqueta_rojo = tkinter.Label(ventana, text="posicionamiento absoluto", background="red", foreground="yellow") #Creamos etiqueta
etiqueta_rojo.place(x=10, y=75) #La colocamos y lo rediseñamos en tamaño

etiqueta_verde = tkinter.Label(ventana, text="posicionamiento relativo", background="green", foreground="white") #Creamos etiqueta
etiqueta_verde.place(relx=0.10, rely=0.15) #La colocamos y lo rediseñamos en tamaño

ventana.mainloop() #generamos ventana mendiante un bucle