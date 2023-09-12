import numpy as np
import time

# Ejemplo 1: Bucle for en Python estándar
start_time = time.time()
total = 0
for i in range(1000000):
    total += i
end_time = time.time()
print(f"Tiempo para bucle for en Python estándar: {end_time - start_time} segundos")

# Ejemplo 2: Utilizando NumPy para vectorizar la suma
start_time = time.time()
arr = np.arange(1000000)
total = np.sum(arr)
end_time = time.time()
print(f"Tiempo para NumPy: {end_time - start_time} segundos")

# Ejemplo 3: Realizando una suma simple
start_time = time.time()
total = sum(range(1000000))
end_time = time.time()
print(f"Tiempo para suma simple: {end_time - start_time} segundos")

#####################################################################################

import random

# Generar notas aleatorias para 100 alumnos entre 0 y 100 (puedes ajustar el rango)
notas_alumnos = [random.uniform(0, 100) for _ in range(100)]

# Calcular la media de notas menores a 70 utilizando un bucle for
suma_notas_for = 0
contador_for = 0
for nota in notas_alumnos:
    if nota < 70:
        suma_notas_for += nota
        contador_for += 1

media_for = suma_notas_for / contador_for if contador_for > 0 else 0

# Calcular la media de notas menores a 70 utilizando NumPy
notas_array = np.array(notas_alumnos)
notas_menores_70 = notas_array[notas_array < 70]
media_numpy = np.mean(notas_menores_70)

print(f"Media de notas menores a 70 utilizando un bucle for: {media_for}")
print(f"Media de notas menores a 70 utilizando NumPy: {media_numpy}")
