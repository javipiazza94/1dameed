import tkinter as tk

def show_selected():
    label_texto.config(text="Elemento seleccionado: " + lista_elementos.get(lista_elementos.curselection()))

ventana = tk.Tk()
ventana.title("Ejemplo de lista y label")

lista_elementos = tk.Listbox(ventana)
lista_elementos.insert(1, "Elemento 1")
lista_elementos.insert(2, "Elemento 2")
lista_elementos.insert(3, "Elemento 3")
lista_elementos.pack()

label_texto = tk.Label(ventana, text="Selecciona un elemento de la lista")
label_texto.pack()

boton = tk.Button(ventana, text="Mostrar selección", command=show_selected)
boton.pack()

ventana.mainloop()
