import tkinter

ventana = tkinter.Tk()

Etiqueta = tkinter.Label(ventana, text = "UNA", bg = "Red", fg = "white")# En los parametros colocamos donde queremos situarla, texto descriptivo y propiedades (background color, foreground color)
Etiqueta.pack(ipadx=150, ipady = 50, fill="both") #Rellenamos los parametros con el padding y el relleno, mas otras propiedades como expand o side
Etiqueta2 = tkinter.Label(ventana, text = "GRANDE", bg = "Yellow", fg = "Red") #El pack es una geometria para distribuir de arriba a abajo, y de izqda a drcha
Etiqueta2.pack(ipadx=300, ipady=100, fill="both", expand=True)
Etiqueta3 = tkinter.Label(ventana, text = "LIBRE", bg = "Red", fg = "white")
Etiqueta3.pack(ipadx=150, ipady=50, fill="both")

ventana.mainloop()