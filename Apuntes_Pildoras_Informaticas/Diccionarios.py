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
print(Palmares.keys()) #devuelve las claves
print(Palmares.values()) #devuelve los valores
print(len(Palmares)) #devuelve la longitud
