import pickle

lista_nombres = ["Alonso", "Verstappen", "Hamilton", "Russel", "Sainz", "Perez", "Leclerc"]

archivo_lista = open("lista", "wb+")

pickle.dump(lista_nombres, archivo_lista)

archivo_lista.close()