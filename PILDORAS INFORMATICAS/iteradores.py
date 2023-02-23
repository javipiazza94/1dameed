from itertools import cycle
from itertools import islice
from itertools import count

#iterador 1
iter1 = iter([1,2,3])
print(type(iter1))
print(next(iter1))

#iterador 2
iter2 = iter("hola")
print(type(iter2))

#iterador 3
iter3 = reversed([3,4,5])
print(next(iter3))

#iterador 4
colors = cycle(['red', 'white', 'blue'])
print(next(colors))
limited = islice(colors, 0, 4) 
for x in limited:
    print(x) 

#iterador 5
counter = count(start=13)
print(next(counter))

