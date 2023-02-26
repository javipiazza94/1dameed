cadena = "En un lugar de la Mancha"
print(cadena.title())
print(cadena.lower())
print(cadena.upper())
print(cadena.lower().count('a')) #Cuenta el numero de 'a' minusculas
print(cadena.split()) # Separa las cadenas en una lista
print(cadena.startswith("En")) #Dice si empieza por X y devuelve true o false
print(cadena.endswith("Papa")) #Dice si termina  por X y devuelve true o false


numero = "      464758"
alfa = '-'
print(alfa.isalpha()) # Si es alfabetico
print(alfa.isalnum()) # Si es alfanumerico
print(numero.isdigit()) # Si es un digito
print(numero.lstrip()) #Quita los espacios iniciales de la cadena
