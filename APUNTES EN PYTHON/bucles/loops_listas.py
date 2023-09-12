planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for planet in planets:
    print(planet, end=' ') # print all on same line

#Multiplicado 
multiplicands = (2, 2, 2, 3, 3, 5)
product = 1
for mult in multiplicands:
    product = product * mult
product

#filtro
s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
msg = ''
# print all the uppercase letters in s, one at a time
for char in s:
    if char.isupper():
        print(char, end='')     

#rangos
#range() is a function that returns a sequence of numbers. It turns out to be very useful for writing loops.
for i in range(5):
    print("Doing important work. i =", i)
    
#bucles condicionales
#The other type of loop in Python is a while loop, which iterates until some condition is met:
i = 0
while i < 10:
    print(i, end=' ')
    i += 1 # increase the value of i by 1
    
#LISTAS COMPRIMIDAS
squares = [n**2 for n in range(10)]
print(squares)
    #Mismo resultado
squares2 = []
for n in range(10):
    squares2.append(n**2)
print(squares2)
    #con if
short_planets = [planet for planet in planets if len(planet) < 6]
print(short_planets)
    #Creamos una lista con funciones y caracteres usando for a partir de otra lista
loud_short_planets = [planet.upper() + '!' for planet in planets if len(planet) < 6]
print(loud_short_planets)
    #Una sola linea
[
    planet.upper() + '!' 
    for planet in planets 
    if len(planet) < 6
]
#Conteo en una lista
def count_negatives(nums):
    """Return the number of negative numbers in the given list.
    
    >>> count_negatives([5, -1, -2, 0, 3])
    2
    """
    n_negative = 0
    for num in nums:
        if num < 0:
            n_negative = n_negative + 1
    return n_negative

def count_negatives(nums):
    return len([num for num in nums if num < 0])

