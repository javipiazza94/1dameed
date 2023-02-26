import tkinter as tk

def mostrar_seleccion():
    print("Selecciona la opcion:", var.get())

def resetear_opciones():
    var.set(0)

ventana = tk.Tk()
ventana.title("RadioButton ejemplo")

var = tk.IntVar()
var.set(0)

opciones = [("Opcion 1", 1), ("Opcion 2", 2), ("Opcion 3", 3)]
for text, value in opciones:
    tk.Radiobutton(ventana, text=text, variable=var, value=value, command=mostrar_seleccion).pack()

tk.Button(ventana, text="Reset", command=resetear_opciones).pack()

ventana.mainloop()
