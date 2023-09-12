import pandas as pd
import numpy as np

#Establecemos el maximo de columnas
pd.set_option('display.max_columns', 20)

#Leemos el archivo
archivo_excel = pd.read_csv('StudentsPerformance.csv')
archivo_excel.reset_index()
archivo_excel = archivo_excel.rename(columns={'gender' : 'sexo'})
print(archivo_excel)

# Filtrar solo las columnas numéricas
columnas_numericas = archivo_excel[['math score', 'reading score', 'writing score']]

#Operaciones basicas --> sum, mean, min, max, min, count
archivo_excel.describe() #--> Por cokumna
    # Suma
#archivo_excel.sum(axis=1) #por fila
print(archivo_excel['math score']+archivo_excel['reading score']+archivo_excel['writing score']) #por fila nombrando a las columnas
    #contador
print(archivo_excel['sexo'].value_counts())
    #media
    # Calcular el promedio de las columnas numéricas y asignarlo a una nueva columna 'average'
archivo_excel['average'] = columnas_numericas.mean(axis=1)
print(archivo_excel['average'])

#Condicionales --> If

#Estructura --> Nombre columna nueva = if (np.where) condicion columna a evaluar, dato a colocar si se cumple, dato si no se cumple
archivo_excel['Aprobado/Suspendo'] = np.where(archivo_excel['average'] > 50, 'Aprobado', 'Suspenso')
print(archivo_excel['Aprobado/Suspendo'])

#Condicionales complejos
condiciones = [
    (archivo_excel['average']>=90),
    (archivo_excel['average']>=80) & (archivo_excel['average']<90),
    (archivo_excel['average']>=70) & (archivo_excel['average']<80),
    (archivo_excel['average']>=60) & (archivo_excel['average']<70),
    (archivo_excel['average']>=50) & (archivo_excel['average']<60),
    (archivo_excel['average']<50),
]
valores = ['Matricula de Honor', 'Sobresaliente', 'Notable', 'Bien', 'Aprobado', 'Suspenso']
archivo_excel['Resultados'] = np.select(condiciones, valores)
print(archivo_excel['Resultados'])


#sumif, countif, avgif
#Promedio sexo femenino
    #Imprimimo columna femenina y de razas y hago media
tabla_femenina = archivo_excel[archivo_excel['sexo'] == 'female']
tabla_razas = archivo_excel[archivo_excel['race/ethnicity'] == 'group A']
tabla_femenina['media'] = (archivo_excel['math score']+archivo_excel['reading score']+archivo_excel['writing score']).mean() #solo las columnas con enteros
print(tabla_femenina)

#Promedio multiple y sumas
tabla_multiple = archivo_excel[(archivo_excel['sexo'] == 'female') & (archivo_excel['race/ethnicity'] == 'group A')]
tabla_multiple['sumas'] = tabla_multiple['math score']+tabla_multiple['reading score']+tabla_multiple['writing score']
print(tabla_multiple)

#Busquedas
    #metodo loc[fila, columna]
print(archivo_excel.loc[45, 'parental level of education'])
    #Con condiciones
print(archivo_excel.loc[archivo_excel['sexo']== 'male'], 'math score')   

#tablas dinamicas
tabla = archivo_excel.pivot_table(index = 'race/ethnicity', values = ['math score', 'writing score'], aggfunc = 'mean')
print(tabla)

#Extraer Strings
Strings = archivo_excel['race/ethnicity'].str.extract('r([A-Z])')
print(Strings)

#Valores nulos
nulos = archivo_excel['race/ethnicity'].isnull()
print(nulos)

#Mayusculas y minusculas
print(tabla_femenina['sexo'].str.capitalize())
print(tabla_femenina['sexo'].str.upper())
print(tabla_femenina['sexo'].str.title())

"""
#Rellenar
archivo_excel = archivo_excel.fillna('0')
archivo_excel = archivo_excel['race/ethnicity'].fillna('morapio', inplace=True)
"""

import matplotlib.pyplot as plt

#Graficos
tabla_indexada = tabla.reset_index()
print(tabla_indexada)

#barplot
barras = plt.bar(tabla_indexada['race/ethnicity'], tabla_indexada['math score'])
plt.show()








