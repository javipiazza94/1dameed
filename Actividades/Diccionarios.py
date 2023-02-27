#  Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada palabra en la cadena. Por ejemplo, si recibe “Qué lindo día que hace hoy” debe devolver: ‘que’: 2, ‘lindo’: 1, ‘día’: 1, ‘hace’: 1, ‘hoy’: 1
diccionario = {}
frase = input("Introduce la frase: ")
lista_palabras = frase.split(" ")
contador = 1
for palabra in lista_palabras:
    if palabra in diccionario:
        diccionario[palabra] += contador
    else:
        diccionario[palabra] = contador
    contador += 1

for palabra, cantidad in diccionario.items():
    print(f"{palabra}: {cantidad}")

# Tenemos guardado en un diccionario los códigos morse corespondientes a cada caracter. Escribir un programa que lea una palabra y la muestre usando el código morse.
codigo = {
    'A': '.-',     'B': '-...',    'C': '-.-.',
    'D': '-..',    'E': '.',       'F': '..-.',
    'G': '--.',    'H': '....',    'I': '..',
    'J': '.---',   'K': '-.-',     'L': '.-..',
    'M': '--',     'N': '-.',      'O': '---',
    'P': '.--.',   'Q': '--.-',    'R': '.-.',
    'S': '...',    'T': '-',       'U': '..-',
    'V': '...-',   'W': '.--',     'X': '-..-',
    'Y': '-.--',   'Z': '--..',    '1': '.----',
    '2': '..---',  '3': '...--',   '4': '....-',
    '5': '.....',  '6': '-....',   '7': '--...',
    '8': '---..',  '9': '----.',   '0': '-----',
    '.': '.-.-.-', ',': '--..--',  ':': '---...',
    ';': '-.-.-.', '?': '..--..',  '!': '-.-.--',
    '"': '.-..-.', "'": '.----.',  '+': '.-.-.',
    '-': '-....-', '/': '-..-.',   '=': '-...-',
    '_': '..--.-', '$': '...-..-', '@': '.--.-.',
    '&': '.-...',  '(': '-.--.',   ')': '-.--.-'
} 

Palabra_morse = input("Escribe la palabra: ")
lista_codigos = []
for caracter in Palabra_morse:
    if caracter.islower():
        caracter=caracter.upper()
    lista_codigos.append(codigo[caracter])    
print (" ".join(lista_codigos))

#Continuar el programa: ahora nos pide un cóigo morse donde cada letra esta separada por espacios y nos da la cadena correspondiente.
morse=input("Morse:")
lista_morse=morse.split(" ")
palabra = ""
for cod in lista_morse:
    letra=[key for key,valor in codigo.items() if valor==cod][0]
    palabra=palabra+letra
print (palabra)

#Suponga un diccionario que contiene como clave el nombre de una persona y como valor una lista con todas sus “gustos”. Desarrolle un programa que agregue “gustos” a la persona:
"""
Si la persona no existe la agregue al diccionario con una lista que contiene un solo elemento.
Si la persona existe y el gusto existe en su lista, no tiene ningún efecto.
Si la persona existe y el gusto no existe en su lista, agrega el gusto a la lista.
Se deja de pedir personas cuando introducimos el carácter “*”. """

gustos={}
nombre = input("Nombre:")
while nombre!="*":
    gusto=input("Gusto:")
    lista_gustos=gustos.setdefault(nombre,[gusto])
    if lista_gustos!=[gusto]:
        gustos[nombre].append(gusto)
    nombre = input("Nombre:")
print(gustos)