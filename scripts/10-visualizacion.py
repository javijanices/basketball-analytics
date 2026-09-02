import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/raw/partidos.csv", sep=";")


# Grafico 1 - promedio de puntos por jugador, grafico de barras
fig, ax = plt.subplots(figsize=(8, 5))
promedios_p = df.groupby("Jugador", as_index=False)["Puntos"].mean()
promedio_puntos_ordenados = promedios_p.sort_values(by="Puntos", ascending=False)
promedio_puntos_ordenados.plot(x='Jugador', y='Puntos', kind='bar', ax=ax, color='skyblue', legend=False)
ax.bar_label(ax.containers[0], padding=3, fmt='%.2f')

plt.title("Promedio de puntos por jugador")
plt.xlabel("Jugador")
plt.ylabel("Puntos promedio")
plt.tight_layout()  #Evita que títulos, etiquetas o nombres queden cortados cuando exportemos los gráficos
plt.savefig(
    "images/promedio_puntos.png",
    dpi = 300,
    bbox_inches = "tight"
)
plt.show()  

# Grafico 2 - Evolucion de puntos del jugador Ezequiel partido a partido, tipo linea
ezequiel = df[df["Jugador"] == "Ezequiel"]
ezequiel.plot(x="Partido", y="Puntos", kind="line", marker="o", color='green', legend=False)

plt.title("Evolucion de puntos del jugador Ezequiel por partido")
plt.xlabel("Partido")
plt.ylabel("Puntos convertidos")
plt.xticks(ezequiel["Partido"])
plt.tight_layout()
plt.savefig(
    "images/evolucion_ezequiel.png",
    dpi = 300,
    bbox_inches = "tight"
)
plt.show() 

# Grafico 3 - comparacion de promedios de Puntos, Rebotes y Asistencias por jugador
estadisticas = df.groupby("Jugador", as_index=False)[['Puntos', 'Rebotes', 'Asistencias']].mean()
estadisticas.plot(x="Jugador", y=["Puntos", "Rebotes", "Asistencias"], kind='bar')

plt.title("Promedios estadisticos de cada jugador")
plt.xlabel("Jugador")
plt.ylabel("Promedios")
plt.tight_layout()
plt.savefig(
    "images/comparacion_estadisticas.png",
    dpi = 300,
    bbox_inches = "tight"
)
plt.show()
