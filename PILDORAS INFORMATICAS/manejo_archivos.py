from io import open

#modos de texto --> w, a, r (escritura, añadir, lectura)

archivo_texto = open("pruebas.txt", "r+")
lectura = archivo_texto.readlines() #lee en lista por linea
print(lectura[0])
print(lectura[1])

"""archivo_texto = open("pruebas.txt", "a")
#archivo_texto.write("\n JENNI A PRISION")
archivo_texto = open("pruebas.txt", "r")
lectura = archivo_texto.readlines() #lee en lista por linea"""

archivo_texto.seek(len(archivo_texto.read())/2) #pongo un cursor y lo leo a la mitad de su longitud
print(archivo_texto.read())
archivo_texto.close()


    