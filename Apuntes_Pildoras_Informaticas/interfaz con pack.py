import tkinter #importamos libreria

ventana = tkinter.Tk() #inicializamos objeto ventana

#Geometría pack: de izquierda a derecha o de arriba a abajo
etiqueta_rojo = tkinter.Label(ventana, text="VIVA", background="red", foreground="yellow") #Creamos etiqueta
etiqueta_rojo.pack( ipadx=100, ipady=75, fill="both") #La colocamos y lo rediseñamos en tamaño
etiqueta_amarillo = tkinter.Label(ventana, text="CRISTO", background="yellow", foreground="red") #Creamos etiqueta
etiqueta_amarillo.pack( ipadx=100, ipady=100, fill="both") #La colocamos y lo rediseñamos en tamaño
etiqueta_rojo2 = tkinter.Label(ventana, text="REY", background="red", foreground="yellow") #Creamos etiqueta
etiqueta_rojo2.pack( ipadx=100, ipady=75, fill="both") #La colocamos y lo rediseñamos en tamaño
#Otras propiedades: expand(true o false), side("left" o "right")

ventana.mainloop() #generamos ventana mendiante un bucle