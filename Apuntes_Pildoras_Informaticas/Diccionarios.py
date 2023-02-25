diccionario = {"Somalia": "Mogadiscio","Mongolia": "Ulan Bathor", "Albania": "Skopye"}
diccionario["Hitler"]=88 #Asi se anaden dato, y para cambiarla se sobreescribe
print(diccionario)
print(diccionario["Somalia"]) #Pedimos la clave y nos da el valor
del diccionario["Albania"] #Para borrar un elemento
print(diccionario)

#Diccionarios y tuplas
tupla = ["Arriba", "Heil", "El autentico socialismo"]
diccionario_de_tupla = {tupla[0]:"Espana", tupla[1]:"Hitler", tupla[2]:"el nacional"} #metemos los valores de un diccionario a una tupla
print(diccionario_de_tupla)
Palmares = {"nombre": "Rafa Nadal", "Grand Slams":{"numero": 22}, "Open de Australia": [2009, 2022], "Wimbledon": [2008, 2010], "Roland Garros": [2005, 2006, 2007, 2008, 2010, 2011, 2012, 2013, 2014, 2017, 2018, 2019, 2020, 2022], "US Open": [2010, 2013, 2017, 2019] }
print(Palmares)
print(Palmares.keys()) #devuelve las claves y se pueden guardar en variables
print(Palmares.values()) #devuelve los valores y se pueden guardar en variables
print(len(Palmares)) #devuelve la longitud

#Diccionarios complejos
Alumno = {"nombre": "Alejandro", "edad": 22, "direccion":{"Calle": "Francisco Franco", "numero": 36, "Codigo Postal":1041936}, "notas": (8,7,9,10,10,5)}
print(Alumno)
print(Alumno["notas"][3]) #Para acceder a un campo especifico

#Otros metodos
dict1 = {}
print(dir(dict1)) #Averiguar metodos
dict1 = dict(one=1, two=2, three=3)
dict2 = dict1.copy() #Copiar diccionarios
print(dict1)
dict1.clear() #Borrar contenido del diccionario
print(dict1)
dict1 = dict(one=1, two=2, three=3)
dict2 = {'four':4,'five':5}
dict1.update(dict2) #Anadir un diccionario en otro
print(dict1)
print(dict1.get("one")) #Obtenemos el valor
dict1 = dict.fromkeys(["one", "two", "three"], 100) #Anadimos el mismo valor a las claves
print(dict1)
dict2.setdefault("six",6 ) #Anade una pareja si no existe
print(dict2)
print(dict2.pop("four")) #Devuelve el valor y lo elimina del diccionario
print(dict2)
print(dict2.items()) #Devuelve un objeto dict_items con los valores del diccionario

#Recorrido de claves y valores con un for
for claves in dict2.keys():
    print(claves)
    
for valores in dict2.values():
    print(valores)
    
for claves, valores in dict1.items():
    print(claves, valores)


