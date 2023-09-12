numbers = {'one':1, 'two':2, 'three':3}
numbers['one']
numbers['eleven'] = 11
numbers['eleven'] = "ESPAÑA"
for k in numbers:
    print("{} = {}".format(k, numbers[k]))
    
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[0] for planet in planets}
print(planet_to_initial)
# Get all the initials, sort them alphabetically, and put them in a space-separated string.
iniciales = ' '.join(sorted(planet_to_initial.values()))
print(iniciales)
for planet, initial in planet_to_initial.items():
    print("{} begins with \"{}\"".format(planet.rjust(10), initial))
