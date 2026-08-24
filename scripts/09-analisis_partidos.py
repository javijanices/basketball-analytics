import pandas as pd

df = pd.read_csv("data/raw/partidos.csv", sep=";")

print(f"1- El dataset tiene {df.shape[0]} filas y {df.shape[1]} columnas")

print(f"2- Los nombres de las columnas son: ", df.columns)

print(f"3- Cada columna tiene los siguientes tipos de datos: ", df.dtypes)

print(f"4- Hay valores considerado nulos? : ", df.isnull().sum())

print(f"5- La cantidad de partidos disputados es: ", df["Partido"].nunique())

print(f"6- La cantidad de jugadores utilizados en el equipo son: ", df["Jugador"].nunique())

# Desafio A - Calculo de puntos totales de cada jugador ordenados de mayor a menor (total points in order - tpio)
total_points = df.groupby("Jugador", as_index=False) ["Puntos"].sum()
total_points_in_order = total_points.sort_values(by="Puntos", ascending=False)
print(f"El total de puntos por jugador es: ")
print(total_points_in_order)

# Desafio B - Promedios de puntos de cada jugador ordenados de mayor a menor (average points in order - apio)
promedios_p = df.groupby("Jugador", as_index=False)["Puntos"].mean()
promedio_puntos_ordenados = promedios_p.sort_values(by="Puntos", ascending=False)
print(f"El promedio de puntos por jugador es: ")
print(promedio_puntos_ordenados)

# Desafio C - Tabla por jugador de multiples estadisticas
estadisticas = df.groupby("Jugador", as_index=False)[['Puntos', 'Rebotes', 'Asistencias']].mean()
print(f"El promedio de puntos, rebotes y asistencias de cada jugador es:")
print(estadisticas)

# Desafio D - Partido de mayor goleo de cada jugador
indices_maximos = df.groupby('Jugador')['Puntos'].idxmax()
maximos_goleos = df.loc[indices_maximos]
max_gol_ordenado = maximos_goleos.sort_values(by='Puntos', ascending=False)
print(max_gol_ordenado[['Partido', 'Jugador', 'Puntos', 'Rival']])

# Desafio E - Crear Valoracion
df['Valoracion'] = (df['Puntos'] + df['Rebotes'] + df['Asistencias'])
max_valoracion = df.loc[df['Valoracion'].idxmax()]
print(f"El partido de mayor valoracion es :")
print(max_valoracion)

# Desafio Extra - Valoracion por promedio ordenado de mayor a menor
promedios_v = df.groupby("Jugador", as_index=False)['Valoracion'].mean()
valoracion_promedio_ordenada = promedios_v.sort_values(by='Valoracion', ascending=False)
print(f"El promedio de valoracion de cada jugador es: ")
print(valoracion_promedio_ordenada)

# BONUS - Observacion del Analisis

"""El mayor goleador en promedio fue Ezequiel con 23.2 puntos, y la mayor valoracion promedio es de Gaston con 38.6. Esto indica
que en este caso el mayor anotador no siempre es quien mas aporta al equipo, Gaston fue el jugador que tuvo en general mejores
numeros estadisticos en promedio"""
