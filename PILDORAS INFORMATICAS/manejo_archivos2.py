from io import open

archivo = open("pruebas2.txt","r+")

nuevo_texto = archivo.readlines()

nuevo_texto[1] = "Verstappen\n"

archivo.seek(0)

lista = archivo.writelines(nuevo_texto)

archivo.close()