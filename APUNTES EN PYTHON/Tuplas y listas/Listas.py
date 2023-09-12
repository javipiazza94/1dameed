#listas de listas
hands = [
    ['J', 'Q', 'K'],
    ['2', '2', '2'],
    ['6', 'A', 'K'], # (Comma after the last element is optional)
]
# (I could also have written this on one line, but it can get hard to read)
hands = [['J', 'Q', 'K'], ['2', '2', '2'], ['6', 'A', 'K']]

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

#Listas de diferentes elementos
my_favourite_things = [32, 'raindrops on roses', help]
# (Yes, Python's help function is *definitely* one of my favourite things)

#recorriendo listas
print(planets[-1])
print(planets[1])
print(planets[0:3])
print(planets[:3])
print(planets[3:])
# All the planets except the first and last
print(planets[1:-1])
# The last 3 planets
print(planets[-3:])

#Modificando listas
planets[3] = 'Malacandra'
planets[:3] = ['Mur', 'Vee', 'Ur']
print(planets)
# That was silly. Let's give them back their old names
planets[:4] = ['Mercury', 'Venus', 'Earth', 'Mars',]

#Funciones
# How many planets are there?
len(planets)
# The planets sorted in alphabetical order
sorted(planets)
primes = [2, 3, 5, 7]
sum(primes)
max(primes)
# Pluto is a planet darn it!
planets.append('Pluto')
planets.pop()
planets.index('Earth')


#Interludio: objetos
x = 12
# x is a real number, so its imaginary part is 0.
print(x.imag)
# Here's how to make a complex number, in case you've ever been curious:
c = 12 + 3j
print(c.imag)
x.bit_length()
help(x.bit_length)

#Rastreo
# Is Earth a planet?
"Earth" in planets
# Is Calbefraques a planet?
"Calbefraques" in planets

#Tuplas
t = (1, 2, 3)
x = 0.125
x.as_integer_ratio()
numerator, denominator = x.as_integer_ratio()
print(numerator / denominator)

#swaping dos variables
a = 1
b = 0
a, b = b, a
print(a, b)

