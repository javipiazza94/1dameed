import pandas as pd
import matplotlib.pyplot as plt

# Definir los datos iniciales
poblacion_total = 1950000
poblacion_extranjeros = 95000
tasa_crecimiento_extranjeros = 0.10

# Crear listas para almacenar los datos de cada año
anios = list(range(2019, 2031))
poblacion_nacionales = [poblacion_total - poblacion_extranjeros]
poblacion_extranjera = [poblacion_extranjeros]
poblacion_total_lista = [poblacion_total]
porcentaje_extranjeros_lista = [(poblacion_extranjeros / poblacion_total) * 100]

for i in range(11):
    poblacion_extranjeros = poblacion_extranjeros * (1 + tasa_crecimiento_extranjeros)
    poblacion_total = poblacion_nacionales[-1] + poblacion_extranjeros
    poblacion_extranjera.append(poblacion_extranjeros)
    poblacion_total_lista.append(poblacion_total)
    poblacion_nacionales.append(poblacion_nacionales[-1])
    porcentaje_extranjeros_lista.append((poblacion_extranjeros / poblacion_total) * 100)
    

# Crear un DataFrame con los datos
data = {'Año': anios, 'Población Nacional': poblacion_nacionales, 'Población Extranjera': poblacion_extranjera,
        'Población Total': poblacion_total_lista, 'Porcentaje de Extranjeros': porcentaje_extranjeros_lista}
df = pd.DataFrame(data)

# Mostrar el DataFrame
print(df)

# Crear el gráfico de barras
plt.figure(figsize=(10, 6))  # Tamaño del gráfico
plt.bar(anios, poblacion_nacionales, label='Población Nacional', color='blue', alpha=0.7)
plt.bar(anios, poblacion_extranjera, label='Población Extranjera', color='red', alpha=0.7, bottom=poblacion_nacionales)

# Personalizar el gráfico
plt.xlabel('Año')
plt.ylabel('Población')
plt.title('Población Nacional vs. Población Extranjera en Sevilla (2019-2030)')
plt.legend()

# Mostrar el gráfico
plt.show()


