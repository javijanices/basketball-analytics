jugadores = ["Juan", "Gaston", "Ezequiel", "Elian", "Feliciano"]
puntos = [15, 22, 25, 10, 6]

for jugador, punto in zip(jugadores, puntos):
    print(f"El jugador {jugador} convirtio {punto} puntos")

print(f"El total de puntos del Equipo fue ", sum(puntos))

print(f"El promedio de puntos por jugador del Equipo fue de", sum(puntos)/len(jugadores))

ganador, max_puntos = max(zip(jugadores, puntos), key=lambda x: x[1])
print(f"El maximo anotador del Equipo fue {ganador} con {max_puntos} puntos.")