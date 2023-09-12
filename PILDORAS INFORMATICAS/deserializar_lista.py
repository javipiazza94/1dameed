import pickle

try:
    with open("lista", "rb") as archivo_lista:
        lista_nombres = pickle.load(archivo_lista)
        print(lista_nombres)
except FileNotFoundError:
    print("El archivo 'lista' no se encuentra en la ubicación especificada.")
except Exception as e:
    print(f"Ocurrió un error al cargar el archivo: {e}")


