import pandas as pd

df = pd.read_csv("data/raw/jugadores.csv", sep=";")

# PARTE 1 Carga e Inspección

print(f"1- El dataset tiene {df.shape[0]} filas y {df.shape[1]} columnas")

print(f"2- Los nombres de las columnas son: ", df.columns)

print(f"3- Cada columna tiene los siguientes tipos de datos: ", df.dtypes)

print(f"4- Hay valores considerado nulos? : ", df.isnull().sum())

# imprimir resumen rapido y total del dataframe
#print(df.info())

# imprimir los primeros valores
print(f"5- Las primeras filas del dataset son: ", df.head())

# PARTE 2 ANALISIS

total = df["Puntos"].sum()
print(f"El total de puntos del equipo es: ", total)

prom_p = df["Puntos"].mean()
print(f"El promedio de puntos del equipo es: ", prom_p)

max_p = df["Puntos"].max()
print(f"La mayor cantidad de puntos convertidos es:", max_p)

min_p = df["Puntos"].min()
print(f"La menor cantidad de puntos convertidos es:", min_p)

prom_r = df["Rebotes"].mean()
print(f"El promedio de rebotes del equipo es: ", prom_r)

prom_a = df["Asistencias"].mean()
print(f"El promedio de asistencias del equipo es: ", prom_a)

# PARTE 3

#ordenar el dataset de mayor a menor segun puntos convertidos
df_ordenado = df.sort_values(by="Puntos", ascending=False)
print(f"Top 3 ANOTADORES")
print(df_ordenado[['Jugador', 'Puntos']].head(3))

#creacion de la columna valoracion
df_ordenado['Valoracion'] = (df_ordenado['Puntos'] + df_ordenado['Rebotes'] + df_ordenado["Asistencias"])
print(df_ordenado)

