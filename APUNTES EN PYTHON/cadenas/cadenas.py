#cadenas

x = 'Pluto is a planet'
y = "Pluto is a planet"
x == y

pluto = 'Pluto\'s a planet!'
print(pluto)
"""
    The table below summarizes some important uses of the backslash character.

What you type...	What you get	example	print(example)
\'	'	'What\'s up?'	What's up?
\"	"	"That's \"cool\""	That's "cool"
\\	\	"Look, a mountain: /\\"	Look, a mountain: /\
\n	"1\n2 3"	1
                2 3
    
"""

#Secuencias de caracteres
planet = 'Pluto'
print(planet[0])
# Yes, we can even loop over them
[char+'! ' for char in planet]

#metodos
claim = "Pluto is a planet!"
claim.capitalize()
claim.lower()
claim.upper()
claim.index('plan')
len(claim)
words = claim.split() 
print(words)

datestr = '1956-01-31'
year, month, day = datestr.split('-')
print(year, month, day)
union_guion = '/'.join([month, day, year])
print(union_guion)
unicode = ' 👏 '.join([word.upper() for word in words])
print(unicode)

#Building strings with .format()
print(planet + ', we miss you.')
position = 9
print(planet + ", you'll always be the " + str(position) + "th planet to me.")
print("{}, you'll always be the {}th planet to me.".format(planet, position))

pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390
#         2 decimal points   3 decimal points, format as percent     separate with commas
pluto_description = "{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(
    planet, pluto_mass, pluto_mass / earth_mass, population,
)
print(pluto_description)

# Referring to format() arguments by index, starting from 0
s = """Pluto's a {0}.
No, it's a {1}.
{0}!
{1}!""".format('planet', 'dwarf planet')
print(s)




